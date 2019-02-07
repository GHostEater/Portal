# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from accounts.admin import admin_site
from paymentwaving.models import WavedPayment

# Register your models here.


class WavedPaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_type', 'student', 'level', 'waved_by')
    search_fields = ('payment_type__name',
                     'student__user__username',
                     'student__user__first_name',
                     'student__user__last_name',
                     'level__level',
                     'waved_by__user__first_name',
                     'waved_by__user__last_name',
                     )


admin_site.register(WavedPayment, WavedPaymentAdmin)
