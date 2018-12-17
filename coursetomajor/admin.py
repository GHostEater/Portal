# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from coursetomajor.models import CourseToMajor

# Register your models here.


class CourseToMajorAdmin(admin.ModelAdmin):
    list_display = ("course", "major", 'level')
    search_fields = (
        "course__title",
        "course__code",
        'major__name',
        'major__dept__name',
        'major__dept__college_name',
        'level__level',
    )

admin.site.register(CourseToMajor, CourseToMajorAdmin)
