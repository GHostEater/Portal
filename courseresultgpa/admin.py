# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from accounts.admin import admin_site
from courseresultgpa.models import CourseResultGPA

# Register your models here.


class CourseResultGPAAdmin(admin.ModelAdmin):
    list_display = ('student', 'tcp', 'tnu', 'gpa', 'ctcp', 'ctnu', 'cgpa', 'tce', 'status', 'rel', 'session', 'semester')

admin_site.register(CourseResultGPA, CourseResultGPAAdmin)
