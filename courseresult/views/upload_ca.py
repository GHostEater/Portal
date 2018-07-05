# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import Student
from course.models import Course
from courseresult.models import CourseResult
from dept.models import Dept
from session.models import Session


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_ca(request):
    data = request.data
    processed = 0

    for i, d in enumerate(data):
        student = Student.objects.get(pk=d['student'])

        course = Course.objects.get(pk=d['course'])
        if d['ca'] >= course.ca:
            ca = course.ca
        else:
            ca = d['ca']

        result = CourseResult()
        result.ca = ca
        result.student = student
        result.dept = Dept.objects.get(pk=d['dept'])
        result.course = course
        result.session = Session.objects.get(pk=d['session'])
        try:
            result.save()
        except:
            continue
        processed = i

    ret = {
        'processed': processed
    }
    return Response(ret)
