# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from courseresult.models import CourseResult, ReleaseStatus


# Register your models here.


class CourseResultAdmin(admin.ModelAdmin):
    list_display = ("student", "course", 'ca', 'exam', 'final', 'grade', 'gp', 'session', 'rel', 'status')

admin.site.register(CourseResult, CourseResultAdmin)
admin.site.register(ReleaseStatus)
