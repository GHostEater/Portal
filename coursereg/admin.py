# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from coursereg.models import CourseReg

# Register your models here.


class CourseRegAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "session", "level")
    search_fields = ("student__user__last_name",
                     "student__user__first_name",
                     "student__user__username",
                     "student__user__email",
                     "course__code",
                     "course__title",
                     "session__session",
                     "level__level",)

admin.site.register(CourseReg, CourseRegAdmin)
