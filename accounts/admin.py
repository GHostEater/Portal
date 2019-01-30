# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from accounts.models import User, CollegeOfficer, StudentAffairs, AcademicAffairs, Bursar, Lecturer, Student, Unit, Dean

admin.site.site_header = "Summit API"
admin.site.index_title = "Administration"
admin.site.site_title = "Summit API"


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "last_name", "first_name", "email", "type", "unit")
    search_fields = ("username", "last_name", "first_name", "email", "type", 'unit__name')


class StudentAdmin(admin.ModelAdmin):
    list_display = ("user", 'major', 'level', 'mode_of_entry', 'status', 'programme_type')
    search_fields = (
        "major__name",
        "major__dept__name",
        "major__dept__college__name",
        "user__username",
        "user__last_name",
        "user__first_name",
        "user__email",
        "user__type",
        "user__unit__name",
        "level__level",
        "mode_of_entry__name",
        "status",
        "programme_type",
    )

admin.site.register(User, UserAdmin)
admin.site.register(CollegeOfficer)
admin.site.register(StudentAffairs)
admin.site.register(AcademicAffairs)
admin.site.register(Bursar)
admin.site.register(Lecturer)
admin.site.register(Student, StudentAdmin)
admin.site.register(Unit)
admin.site.register(Dean)
