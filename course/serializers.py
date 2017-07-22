from rest_framework import serializers
from course.models import Course


class CourseSerializer(serializers.ModelSerializer):
    level = serializers.SerializerMethodField()
    dept = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_level(self, obj):
        return str(obj.level.level)

    def get_dept(self, obj):
        return str(obj.dept.name)
