# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from accounts.models import User, CollegeOfficer, StudentAffairs, AcademicAffairs, Bursar, Lecturer, Student, Unit, Dean

admin.site.site_header = "Fountain API"
admin.site.index_title = "Administration"
admin.site.site_title = "Fountain API"


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "last_name", "first_name", "type", "unit")
    search_fields = ("username", "last_name", "first_name", "type", "email")

admin.site.register(User, UserAdmin)
admin.site.register(CollegeOfficer)
admin.site.register(StudentAffairs)
admin.site.register(AcademicAffairs)
admin.site.register(Bursar)
admin.site.register(Lecturer)
admin.site.register(Student)
admin.site.register(Unit)
admin.site.register(Dean)
