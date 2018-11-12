# -*- coding: utf-8 -*-
from __future__ import print_function

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import Student
from accounts.serializers import StudentSerializer
from coursereg.models import CourseReg
from coursereg.serializers import CourseRegSerializer

from courseresult.models import CourseResult
from courseresult.serializers import CourseResultSerializer
from grade.models import Grade


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def reg_and_raw_results(request):
    data = request.GET
    students = []

    course_reg = CourseRegSerializer.setup_eager_loading(CourseReg.objects
                                                         .filter(course=data['course'], session=data['session']))
    results = CourseResultSerializer.setup_eager_loading(CourseResult.objects
                                                         .filter(course=data['course'], session=data['session']))

    grades = Grade.objects.filter(active=True)

    res = {}
    course_grades = []

    for grade in grades:
        item = {'grade': grade.grade, 'count': results.filter(grade=grade.grade).count()}
        course_grades.append(item)

    res['course_grades'] = course_grades

    _pass = results.filter(status=1).count()

    if _pass == 0 or results.count() == 0:
        pass_percentage = 0
    else:
        pass_percentage = (float(_pass)/float(results.count())) * 100

    for course in course_reg:
        student = Student.objects.get(pk=course.student.pk)
        try:
            result = CourseResultSerializer(results.get(student=student.id)).data
        except ObjectDoesNotExist:
            result = {}

        di = {
            'info': StudentSerializer(student).data,
            'result': result
        }
        students.append(di)

    res['students'] = students
    res['pass_percentage'] = pass_percentage

    return Response(res)
