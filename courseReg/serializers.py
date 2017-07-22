from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from courseReg.models import CourseReg
from course.models import Course
from course.serializers import CourseSerializer
from accounts.models import Student
from accounts.serializers import StudentSerializer


class CourseRegSerializer(serializers.ModelSerializer):
    course = serializers.SerializerMethodField()
    student = serializers.SerializerMethodField()
    level = serializers.SerializerMethodField()
    session = serializers.SerializerMethodField()

    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=CourseReg.objects.all(),
                fields=('course', 'student', 'session')
            )
        ]
        model = CourseReg
        fields = '__all__'

    def get_course(self, obj):
        course = Course.objects.get(pk=obj.course)
        course_s = CourseSerializer(course).data
        return course_s

    def get_student(self, obj):
        student = Student.objects.get(pk=obj.student)
        student_s = StudentSerializer(student).data
        return student_s

    def get_level(self, obj):
        return str(obj.level.level)

    def get_session(self, obj):
        return str(obj.session.session)


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
