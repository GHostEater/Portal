# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from courseReg.forms import CourseToMajorSelectForm
from core.models import Course, College, Dept, Major
from courseReg.models import CourseToMajor

# Create your views here.


@login_required
def course_to_major(request):
    courses = ''
    if request.method == 'POST':
        courses100 = CourseToMajor.objects.filter(major=request.POST['major'], level=1)
        courses200 = CourseToMajor.objects.filter(major=request.POST['major'], level=2)
        courses300 = CourseToMajor.objects.filter(major=request.POST['major'], level=3)
        courses400 = CourseToMajor.objects.filter(major=request.POST['major'], level=4)

        courses = {
            '100': courses100,
            '200': courses200,
            '300': courses300,
            '400': courses400,
        }
    form = CourseToMajorSelectForm()
    return render(request, 'courseReg/course_to_major.html', {'form': form, 'courses': courses})
