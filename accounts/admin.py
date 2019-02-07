# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

from accounts.models import User, CollegeOfficer, StudentAffairs, AcademicAffairs, Bursar, Lecturer, Student, Unit, Dean
from sysinfo.models import SysInfo


class MyAdminSite(AdminSite):

    try:
        sysinfo = SysInfo.objects.get(pk=1)
        site_title = ugettext_lazy(sysinfo.short_name + " API")
        site_header = ugettext_lazy(sysinfo.short_name + " API")
        index_title = ugettext_lazy("Administration")
    except SysInfo.DoesNotExist:
        site_title = ugettext_lazy("API")
        site_header = ugettext_lazy("API")
        index_title = ugettext_lazy("Administration")


admin_site = MyAdminSite()


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

admin_site.register(User, UserAdmin)
admin_site.register(CollegeOfficer)
admin_site.register(StudentAffairs)
admin_site.register(AcademicAffairs)
admin_site.register(Bursar)
admin_site.register(Lecturer)
admin_site.register(Student, StudentAdmin)
admin_site.register(Unit)
admin_site.register(Dean)
