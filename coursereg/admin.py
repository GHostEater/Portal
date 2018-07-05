# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from coursereg.models import CourseReg

# Register your models here.

class CourseRegAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "session", "level")

admin.site.register(CourseReg, CourseRegAdmin)
