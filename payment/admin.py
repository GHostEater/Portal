# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from payment.models import Payment

# Register your models here.


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_type', 'student', 'application', 'transcript_app', 'session', 'level', 'order_id', 'rrr',
                    'date', 'status', 'paid', 'amount')
    search_fields = ('payment_type__name',
                     'student__user__username',
                     'student__user__last_name',
                     'student__user__first_name',
                     'application__first_name',
                     'application__last_name',
                     'transcript_app__last_name',
                     'transcript_app__first_name',
                     'session__session',
                     'level__level',
                     'order_id', 'rrr', 'date', 'status', 'paid', 'amount')


admin.site.register(Payment, PaymentAdmin)
