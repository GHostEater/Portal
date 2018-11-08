# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from admission.models import Application, Pin

# Register your models here.
admin.site.register(Application)
admin.site.register(Pin)
