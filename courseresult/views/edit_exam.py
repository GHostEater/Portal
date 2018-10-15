# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from course.models import Course
from courseresult.models import CourseResult
from courseresult.serializers import CourseResultSerializer
from courseresult.utils import grader


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def edit_exam(request):
    req = request.data

    result = CourseResult.objects.get(pk=req['id'])

    course = Course.objects.get(pk=result.course.id)
    if float(req['exam']) >= course.exam:
        exam = course.exam
    else:
        exam = float(req['exam'])

    if float(result.ca) == -1:
        ca = 0
    else:
        ca = result.ca

    exam_orig = exam
    if exam == -1:
        exam = 0

    print req['exam']
    final = float(ca) + float(exam)
    if final >= 100:
        final = 100

    g = grader(final)
    result.grade = g['grade']
    result.gp = g['gp']
    result.status = g['status']
    result.exam = exam_orig
    result.final = final

    try:
        result.save()
    except:
        result = {}

    return Response(CourseResultSerializer(result).data)