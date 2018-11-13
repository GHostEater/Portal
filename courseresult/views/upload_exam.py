# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import IntegrityError
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import Lecturer
from course.models import Course
from courseresult.models import CourseResult
from courseresult.utils import grader, round_final
from courseresultuploadlog.models import Log
from session.models import Session


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_exam(request):
    req = request.data
    upload = request.data['exam']
    uploaded = ""
    processed = 0
    was_high = False

    for i, d in enumerate(upload):
        try:
            result = CourseResult.objects.get(pk=d['id'])
        except CourseResult.DoesNotExist:
            continue

        if result.exam is not None:
            continue

        course = Course.objects.get(pk=result.course.id)
        if d['exam'] > course.exam:
            exam = course.exam
            was_high = True
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
            uploaded += result.student.user.username + ": " + str(d['exam'])
            if was_high:
                uploaded += " (Higher than Course MAX Score) "
            uploaded += "<br>"
        except IntegrityError:
            continue

        processed = i

    log = Log()
    log.lecturer = Lecturer.objects.get(pk=req['lecturer'])
    log.course = Course.objects.get(pk=req['course'])
    log.session = Session.objects.get(pk=req['session'])
    log.date = datetime.datetime.now()
    log.upload_type = "Exam"
    log.uploaded = uploaded
    log.save()

    ret = {
        'processed': processed
    }
    return Response(ret)
