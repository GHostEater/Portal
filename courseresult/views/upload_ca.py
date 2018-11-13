# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import IntegrityError
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import Student, Lecturer
from course.models import Course
from courseresult.models import CourseResult
from courseresultuploadlog.models import Log
from dept.models import Dept
from level.models import Level
from session.models import Session


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_ca(request):
    req = request.data
    upload = request.data['ca']
    processed = 0
    uploaded = ""
    was_high = False

    for i, d in enumerate(upload):
        student = Student.objects.get(pk=d['student'])

        course = Course.objects.get(pk=d['course'])
        if d['ca'] > course.ca:
            ca = course.ca
            was_high = True
        else:
            ca = d['ca']

        result = CourseResult()
        result.ca = ca
        result.student = student
        result.dept = Dept.objects.get(pk=d['dept'])
        result.course = course
        result.session = Session.objects.get(pk=d['session'])
        result.level = Level.objects.get(pk=student.level.id)
        try:
            result.save()
            uploaded += student.user.username+": "+str(d['ca'])
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
    log.upload_type = "CA"
    log.uploaded = uploaded
    log.save()

    ret = {
        'processed': processed
    }
    return Response(ret)
