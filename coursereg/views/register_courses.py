# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import IntegrityError
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import Student
from course.models import Course
from coursereg.models import CourseReg
from level.models import Level
from session.models import Session


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register_courses(request):
    req = request.data

    student = Student.objects.get(pk=req['student'])
    level = Level.objects.get(pk=req['level'])
    session = Session.objects.get(pk=req['session'])

    for c in req['courses']:
        course = Course.objects.get(pk=c)
        course_reg = CourseReg()
        course_reg.course = course
        course_reg.student = student
        course_reg.level = level
        course_reg.session = session
        try:
            course_reg.save()
        except IntegrityError:
            continue

    return Response({'ok': 'ok'})
