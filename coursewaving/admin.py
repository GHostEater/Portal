# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from coursewaving.models import WavedCourses

# Register your models here.


class WavedCoursesAdmin(admin.ModelAdmin):
    list_display = ("student", "course", 'waved_by')

admin.site.register(WavedCourses, WavedCoursesAdmin)
