from rest_framework import serializers
from courseware.models import Courseware


class CoursewareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courseware
        fields = '__all__'
        depth = 3

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'course',
            'course__level',
            'course__dept',
            'course__dept__college',
        )
        return queryset


class CoursewareCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courseware
        fields = '__all__'
