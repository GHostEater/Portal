# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from course.models import Course
from courseresult.models import CourseResult
from courseresult.utils import grader, round_final


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_exam(request):
    data = request.data
    processed = 0

    for i, d in enumerate(data):
        try:
            result = CourseResult.objects.get(pk=d['id'])
        except CourseResult.DoesNotExist:
            continue

        if result.exam is not None:
            continue

        course = Course.objects.get(pk=result.course.id)
        if d['exam'] >= course.exam:
            exam = course.exam
        else:
            exam = float(d['exam'])

        if float(result.ca) == -1:
            ca = 0
        else:
            ca = result.ca

        exam_orig = exam
        if exam == -1:
            exam = 0

        final = float(ca) + float(exam)
        if final >= 100:
            final = 100.00

        final = round_final(final)

        g = grader(final)
        result.grade = g['grade']
        result.gp = g['gp']
        result.status = g['status']
        result.exam = exam_orig
        result.final = final

        try:
            result.save()
        except:
            continue

        processed = i

    ret = {
        'processed': processed
    }
    return Response(ret)
