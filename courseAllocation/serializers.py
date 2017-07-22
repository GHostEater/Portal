from rest_framework import serializers

from courseAllocation.models import CourseAllocation
from course.models import Course
from accounts.models import Lecturer
from accounts.serializers import LecturerSerializer
from course.serializers import CourseSerializer


class CourseAllocationSerializer(serializers.ModelSerializer):
    course = serializers.SerializerMethodField()
    session = serializers.SerializerMethodField()
    dept = serializers.SerializerMethodField()
    lecturer = serializers.SerializerMethodField()

    class Meta:
        model = CourseAllocation
        fields = '__all__'

    def get_course(self, obj):
        course = Course.objects.get(pk=obj.course.id)
        course_s = CourseSerializer(course).data
        return course_s

    def get_lecturer(self, obj):
        lecturer = Lecturer.objects.get(pk=obj.lecturer.id)
        lecturer_s = LecturerSerializer(lecturer).data
        return lecturer_s

    def get_session(self, obj):
        return str(obj.session.session)

    def get_dept(self, obj):
        return str(obj.dept.name)


class CourseAllocationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseAllocation
        fields = '__all__'
