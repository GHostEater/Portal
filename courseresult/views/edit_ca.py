# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from course.models import Course
from courseresult.models import CourseResult
from courseresult.serializers import CourseResultSerializer
from courseresult.utils import grader, round_final


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def edit_ca(request):
    req = request.data

    result = CourseResult.objects.get(pk=req['id'])

    course = Course.objects.get(pk=result.course.id)
    if float(req['ca']) >= course.ca:
        ca = course.ca
    else:
        ca = float(req['ca'])

    if float(result.exam) == -1:
        exam = 0
    else:
        exam = result.exam

    ca_orig = ca
    if ca == -1:
        ca = 0

    final = float(ca) + float(exam)
    if final >= 100.00:
        final = 100.00

    final = round_final(final)

    g = grader(final)
    result.grade = g['grade']
    result.gp = g['gp']
    result.status = g['status']
    result.ca = ca_orig
    result.final = final

    try:
        result.save()
    except:
        result = {}

    return Response(CourseResultSerializer(result).data)
