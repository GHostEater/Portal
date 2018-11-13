# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template.loader import get_template
from mailqueue.models import MailerMessage
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from courseresult.models import CourseResult
from courseresultgpa.models import CourseResultGPA


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def release_result_and_cgpa(request):
    req = request.GET

    gpas = CourseResultGPA.objects.filter(session=req['session'],
                                          semester=req['semester'],
                                          student__major=req['major'],
                                          student__level=req['level'],
                                          rel=False)
    results = CourseResult.objects.filter(session=req['session'],
                                          course__semester=req['semester'],
                                          student__major=req['major'],
                                          student__level=req['level'],
                                          rel=False)

    for gpa in gpas:
        gpa.rel = True
        gpa.save()

    for result in results:
        result.rel = True
        result.save()

    for gpa in gpas:
        result = results.filter(student=gpa.student.pk)

        template = get_template('result.html')
        context = {"gpa": gpa, "result": result}
        content = template.render(context)

        message = MailerMessage()
        message.subject = str("Results and CGPA for "+gpa.student.user.last_name+", "+gpa.student.user.first_name +
                              " from Fountain University")
        message.to_address = gpa.student.user.email
        if gpa.student.parent_email is not None:
            message.cc_address = gpa.student.parent_email
        message.bcc_address = 'results@fuo.edu.ng'
        message.from_address = 'results@fuo.edu.ng'
        message.content = ""
        message.html_content = content
        message.app = "Fountain University Mailing System"
        message.save()

    return Response({'ok': 'ok'})


def result_test(request):
    gpa = CourseResultGPA.objects.get(student__user__username="NAS-12048")
    result = CourseResult.objects.filter(session=gpa.session,
                                         course__semester=gpa.semester,
                                         student__user__username="NAS-12048")

    return render(request, "result.html", context={"gpa": gpa, "result": result})
