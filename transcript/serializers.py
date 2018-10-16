# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from rest_framework import serializers
from transcript.models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
        depth = 3

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'dept',
            'dept__college',
            'mode_of_entry',
        )
        return queryset


class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
