# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers

from grade.models import GradePoint


class GradePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradePoint
        fields = '__all__'
