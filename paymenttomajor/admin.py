# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from accounts.admin import admin_site
from paymenttomajor.models import PaymentToMajor

# Register your models here.


class PaymentToMajorAdmin(admin.ModelAdmin):
    list_display = ('payment_type', 'major', 'level', 'jme', 'de', 'conversion', 'pt')
    search_fields = ('payment_type__name',
                     'major__name',
                     'major__dept__name',
                     'major__dept__college__name',
                     'major__dept__college__acronym',
                     'level__level',
                     'jme',
                     'de',
                     'conversion',
                     'pt'
                     )


admin_site.register(PaymentToMajor, PaymentToMajorAdmin)
