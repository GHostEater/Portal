from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from course.serializers import CourseSerializer
from course.models import Course
from courseToMajor.models import CourseToMajor


class CourseToMajorSerializer(serializers.ModelSerializer):
    course = serializers.SerializerMethodField()
    major = serializers.SerializerMethodField()
    level = serializers.SerializerMethodField()

    class Meta:
        model = CourseToMajor
        fields = '__all__'

    def get_course(self, obj):
        course = Course.objects.get(pk=obj.course.id)
        course_s = CourseSerializer(course).data
        return course_s

    def get_major(self, obj):
        return str(obj.major.name)

    def get_level(self, obj):
        return str(obj.level.level)


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
