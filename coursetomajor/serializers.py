from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from coursetomajor.models import CourseToMajor


class CourseToMajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseToMajor
        fields = '__all__'
        depth = 3

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'course',
            'course__level',
            'course__dept',
            'course__dept__college',
            'level',
            'major',
            'major__dept',
            'major__dept__college',)
        return queryset


class CourseToMajorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=CourseToMajor.objects.all(),
                fields=('course', 'major')
            )
        ]
        model = CourseToMajor
        fields = '__all__'
