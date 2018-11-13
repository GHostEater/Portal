# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers

from courseresultuploadlog.models import Log


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'
        depth = 3

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'lecturer',
            'lecturer__user',
            'session',
            'course',
        )
        return queryset
