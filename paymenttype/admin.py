# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from paymenttype.models import PaymentType, TuitionFee


# Register your models here.


class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'merchant_id', 'service_type_id', 'api_key', 'admission', 'tuition', 'sex',
                    'incur_charges')
    search_fields = ('name', 'amount', 'merchant_id', 'service_type_id', 'api_key', 'sex')


class TuitionFeeAdmin(admin.ModelAdmin):
    list_display = ('major', 'first', 'second', 'total', 'jme', 'de', 'conversion', 'pt')

admin.site.register(PaymentType, PaymentTypeAdmin)
admin.site.register(TuitionFee, TuitionFeeAdmin)
