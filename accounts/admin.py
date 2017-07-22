# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from accounts.models import User, CollegeOfficer, StudentAffairs, AcademicAffairs, Bursar, Lecturer, Student

admin.site.register(User)
admin.site.register(CollegeOfficer)
admin.site.register(StudentAffairs)
admin.site.register(AcademicAffairs)
admin.site.register(Bursar)
admin.site.register(Lecturer)
admin.site.register(Student)
