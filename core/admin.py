# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from core.models import User, Student, Session, Semester, Level, ModeOfEntry, College, Dept, Major, Course

# Register your models here.


admin.site.register(User)
admin.site.register(Student)
admin.site.register(Dept)
admin.site.register(Session)
admin.site.register(Semester)
admin.site.register(Level)
admin.site.register(ModeOfEntry)
admin.site.register(College)
admin.site.register(Major)
admin.site.register(Course)
