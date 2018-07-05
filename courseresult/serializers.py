from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from courseresult.models import CourseResult, ReleaseStatus


class CourseResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseResult
        fields = '__all__'
        depth = 4

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'course',
            'course__level',
            'course__dept',
            'course__dept__college',
            'student',
            'student__user',
            'student__major',
            'student__major__dept',
            'student__major__dept__college',
            'student__level',
            'student__mode_of_entry',
            'dept',
            'dept__college',
            'session',
        )
        return queryset


class CourseResultCreateSerializer(serializers.ModelSerializer):
    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=CourseResult.objects.all(),
                fields=('student', 'course', 'session')
            )
        ]
        model = CourseResult
        fields = '__all__'


class ReleaseStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReleaseStatus
        fields = '__all__'
