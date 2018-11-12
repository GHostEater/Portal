# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import Student
from coursereg.models import CourseReg
from courseresult.models import CourseResult
from coursetomajor.models import CourseToMajor
from coursetomajor.serializers import CourseToMajorSerializer
from coursewaving.models import WavedCourses
from semester.models import Semester


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def registrable_courses(request):
    req = request.GET
    courses = []
    outstandings = []

    student = Student.objects.get(pk=req['student'])
    semester = Semester.objects.get(pk=1)

    course_to_major = CourseToMajor.objects.filter(major=student.major,
                                                   level__level__lte=student.level.level,
                                                   course__semester=semester.semester)
    registered_courses = CourseReg.objects.filter(student=student.id,
                                                  course__semester=semester.semester,
                                                  session=req['session'])
    result = CourseResult.objects.filter(student=student.id, course__semester=semester.semester)
    wavings = WavedCourses.objects.filter(student=student.id, course__semester=semester.semester)

    semester_courses = course_to_major.filter(level=student.level.id)

    for c in semester_courses:
        try:
            wavings.get(course=c.course.id)
            not_in_wavings = False
        except WavedCourses.DoesNotExist:
            not_in_wavings = True

        try:
            registered_courses.get(course=c.course.id)
            not_in_reg = False
        except CourseReg.DoesNotExist:
            not_in_reg = True

        if not_in_wavings and not_in_reg:
            courses.append(c)

    for c in course_to_major:
        try:
            wavings.get(course=c.course.id)
            not_in_wavings = False
        except WavedCourses.DoesNotExist:
            not_in_wavings = True

        try:
            registered_courses.get(course=c.course.id)
            not_in_reg = False
        except CourseReg.DoesNotExist:
            not_in_reg = True

        try:
            result.exclude(status=0).get(course=c.course.id)
            not_in_result = False
        except CourseResult.DoesNotExist:
            not_in_result = True

        if c in courses:
            not_in_semester_courses = False
        else:
            not_in_semester_courses = True

        if not_in_wavings and not_in_reg and not_in_result and not_in_semester_courses:
            outstandings.append(c)

    return Response({"courses": CourseToMajorSerializer(courses, many=True).data,
                     "outstandings": CourseToMajorSerializer(outstandings, many=True).data})
