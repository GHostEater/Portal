from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from coursereg.models import CourseReg


class CourseRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseReg
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
            'level',
            'session',
        )
        return queryset


class CourseRegCreateSerializer(serializers.ModelSerializer):
    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=CourseReg.objects.all(),
                fields=('course', 'student', 'session')
            )
        ]
        model = CourseReg
        fields = '__all__'
