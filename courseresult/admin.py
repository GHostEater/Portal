# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from accounts.admin import admin_site
from courseresult.models import CourseResult, ReleaseStatus, UploadStatus


# Register your models here.


class CourseResultAdmin(admin.ModelAdmin):
    list_display = ("student", "course", 'ca', 'exam', 'final', 'grade', 'gp', 'session', 'rel', 'status')
    search_fields = ("student__user__last_name",
                     "student__user__first_name",
                     "student__user__username",
                     "student__user__email",
                     "course__code",
                     "course__title",
                     "session__session",
                     "ca",
                     "exam",
                     "final",
                     "grade",
                     "gp",
                     "rel",
                     "status",)

admin_site.register(CourseResult, CourseResultAdmin)
admin_site.register(ReleaseStatus)
admin_site.register(UploadStatus)
