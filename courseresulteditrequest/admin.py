# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from courseresulteditrequest.models import Log, Request

# Register your models here.
admin.site.register(Request)
admin.site.register(Log)
