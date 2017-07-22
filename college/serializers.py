from rest_framework import serializers
from college.models import College


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = [
            'id',
            'name',
            'acronym',
        ]
