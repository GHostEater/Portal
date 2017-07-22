from rest_framework import serializers

from course.serializers import CourseSerializer
from accounts.serializers import StudentSerializer, LecturerSerializer

from courseWaving.models import WavedCourses
from course.models import Course
from accounts.models import Student, Lecturer


class WavedCoursesSerializer(serializers.ModelSerializer):
    course = serializers.SerializerMethodField()
    student = serializers.SerializerMethodField()
    wavedBy = serializers.SerializerMethodField()

    class Meta:
        model = WavedCourses
        fields = '__all__'

    def get_course(self, obj):
        return CourseSerializer(Course.objects.get(pk=obj.course.id)).data

    def get_student(self, obj):
        return StudentSerializer(Student.objects.get(pk=obj.student.id)).data

    def get_wavedBy(self, obj):
        return LecturerSerializer(Lecturer.objects.get(pk=obj.wavedBy.id)).data
