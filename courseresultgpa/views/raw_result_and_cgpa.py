# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import Student
from accounts.serializers import StudentSerializer
from coursereg.models import CourseReg
from courseresult.models import CourseResult
from courseresult.serializers import CourseResultSerializer
from courseresultgpa.models import CourseResultGPA
from courseresultgpa.utils import cgpa_calculator
from coursetomajor.models import CourseToMajor
from coursetomajor.serializers import CourseToMajorSerializer
from coursewaving.models import WavedCourses


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def raw_result_and_cgpa(request):
    req = request.GET
    sick = []
    leave = []
    suspension = []
    deferment = []
    stds = []
    _pass = []
    pcso = []
    probation = []
    withdrawal = []

    results = CourseResult.objects.filter(session=req['session'],
                                          course__semester=req['semester'],
                                          student__major=req['major'],
                                          student__level=req['level'])
    students = Student.objects.filter(major=req['major'], level=req['level'])

    for student in students:
        if student.status == '3':
            leave.append(student)
        elif student.status == '4':
            sick.append(student)
        elif student.status == '5':
            suspension.append(student)
        elif student.status == '6':
            deferment.append(student)
        elif student.status == '1':
            try:
                wavings = WavedCourses.objects.filter(student=student.id)
            except WavedCourses.DoesNotExist:
                wavings = None
            try:
                course_reg = CourseReg.objects.filter(student=student.id)
            except CourseReg.DoesNotExist:
                course_reg = None
            course_to_major = CourseToMajor.objects.filter(major=req['major'],
                                                           level__level__lte=student.level.level,
                                                           course__semester=req['semester'])

            try:
                result = results.filter(student=student.id)
            except CourseResult.DoesNotExist:
                result = None

            std_result = CourseResult.objects.filter(student=student.id)
            std_result_fail = std_result.filter(grade='E')
            fail = []
            outstandings = []

            for res in std_result_fail:
                try:
                    std_result.get(pk=res.pk, status=1)
                    not_in_std_result = False
                except CourseResult.DoesNotExist:
                    not_in_std_result = True
                try:
                    wavings.get(course=res.course.pk)
                    not_in_waving = False
                except WavedCourses.DoesNotExist:
                    not_in_waving = True

                if not_in_std_result and not_in_waving:
                    fail.append(res)

            for course in course_to_major:
                try:
                    course_reg.get(course=course.course.id)
                    not_in_course_reg = False
                except CourseReg.DoesNotExist:
                    not_in_course_reg = True
                try:
                    wavings.get(course=course.course.id)
                    not_in_waving = False
                except WavedCourses.DoesNotExist:
                    not_in_waving = True
                try:
                    result.get(course=course.course.id)
                    not_in_result = False
                except CourseResult.DoesNotExist:
                    not_in_result = True
                not_same_or_lower_level = course.level.level <= student.level.level

                if not_in_course_reg and not_in_waving and not_in_result and not_same_or_lower_level:
                    outstandings.append(course)

                try:
                    in_course_reg = course_reg.get(course=course.course.id)
                except CourseReg.DoesNotExist:
                    in_course_reg = False
                try:
                    no_result_final = result.get(course=course.course.id, final=None)
                except CourseResult.DoesNotExist:
                    no_result_final = False

                if in_course_reg and not_in_waving and (not_in_result or no_result_final):
                    outstandings.append(course)

            try:
                gps = CourseResultGPA.objects.filter(student=student.id).order_by('-session', '-semester')
                if gps.get(session=req['session'], semester=req['semester']):
                    last_gp = gps[1]
                else:
                    last_gp = gps[0]
                gps = CourseResultGPA.objects.filter(student=student.id).order_by('session', 'semester')
            except:
                gps = []
                last_gp = CourseResultGPA()
                last_gp.cgpa = 0
                last_gp.gpa = 0
                last_gp.ctcp = 0
                last_gp.tcp = 0
                last_gp.ctnu = 0
                last_gp.tnu = 0
                last_gp.tce = 0

            prob = 0
            withdraw = 0
            count = 0

            for i in range(0, 2):
                try:
                    if gps[i].cgpa < 1.5:
                        count += 1
                except IndexError:
                    continue
            if count == 2:
                prob = 1
            elif count == 3:
                withdraw = 1
            new_gp = cgpa_calculator(result, last_gp, fail, outstandings)
            status = new_gp['status']
            gp_status = new_gp['status']

            result_obj = CourseResultSerializer(result, many=True).data
            outstandings_obj = CourseToMajorSerializer(outstandings, many=True).data
            fail_obj = CourseResultSerializer(fail, many=True).data

            obj = {
                'info': StudentSerializer(student).data,
                'result': result_obj,
                'resultFail': fail_obj,
                'outstandings': outstandings_obj,
                'tnu': new_gp['tnu'],
                'ctnu': new_gp['ctnu'],
                'tcp': new_gp['tcp'],
                'ctcp': new_gp['ctcp'],
                'tce': new_gp['tce'],
                'gpa': new_gp['gpa'],
                'cgpa': new_gp['cgpa'],
                'prev_cgpa': last_gp.cgpa,
                'prev_ctcp': last_gp.ctcp,
                'prev_ctnu': last_gp.ctnu,
                'prev_tce': last_gp.tce,
                'status': new_gp['status'],
                'gp_status': new_gp['gp_status'],
                'prob': prob,
                'withdraw': withdraw
            }

            if student.level.level == '100':
                if status == 1:
                    _pass.append(obj)
                if status == 0:
                    pcso.append(obj)

            else:
                if (status == 1) and (gp_status <= 2):
                    _pass.append(obj)
                if (status == 0) and (gp_status <= 2):
                    pcso.append(obj)
                if (prob == 1) and (gp_status == 3):
                    probation.append(obj)
                if (withdraw == 1) and (gp_status == 3):
                    withdrawal.append(obj)

            stds.append(obj)

    total = len(_pass) + len(pcso) + len(probation) + len(withdrawal) + len(leave) + len(sick) + len(deferment) + len(suspension)

    response = {
        'students': stds,
        'total': total,
        'pass': _pass,
        'pcso': pcso,
        'probation': probation,
        'withdrawal': withdrawal,
        'leave': leave,
        'sick': sick,
        'deferment': deferment,
        'suspension': suspension
    }

    return Response(response)