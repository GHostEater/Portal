# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from accounts.admin import admin_site
from course.models import Course

# Register your models here.

admin_site.register(Course)
