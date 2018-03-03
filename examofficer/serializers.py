from rest_framework import serializers

from examofficer.models import ExamOfficer


class ExamOfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamOfficer
        fields = '__all__'
        depth = 3

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'lecturer',
            'lecturer__user',
            'lecturer__dept',
            'lecturer__dept__college',
            'dept',
            'dept__college',
        )
        return queryset


class ExamOfficerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamOfficer
        fields = '__all__'
