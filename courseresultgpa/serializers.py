from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from courseresultgpa.models import CourseResultGPA


class CourseResultGPASerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseResultGPA
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
            'student__level',
            'student__mode_of_entry',
            'dept',
            'dept__college',
            'session',
        )
        return queryset


class CourseResultCreateGPASerializer(serializers.ModelSerializer):
    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=CourseResultGPA.objects.all(),
                fields=('student', 'semester', 'session')
            )
        ]
        model = CourseResultGPA
        fields = '__all__'
