# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from transfer.models import IntraUni


class IntraUniSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntraUni
        fields = '__all__'
        depth = 4

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'student',
            'student__user',
            'student__major',
            'student__major__dept',
            'student__major__dept__college',
            'student__mode_of_entry',
            'student__level',
            'major',
            'major__dept',
            'major__dept__college',
            'handled_by',
            'session',
        )
        return queryset


class IntraUniCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntraUni
        fields = '__all__'
