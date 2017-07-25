from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from course.serializers import CourseSerializer
from accounts.serializers import StudentSerializer

from courseResult.models import CourseResult
from course.models import Course
from accounts.models import Student


class CourseResultSerializer(serializers.ModelSerializer):
    course = serializers.SerializerMethodField()
    student = serializers.SerializerMethodField()
    dept = serializers.SerializerMethodField()
    session = serializers.SerializerMethodField()

    class Meta:
        model = CourseResult
        fields = '__all__'

    def get_course(self, obj):
        return CourseSerializer(Course.objects.get(pk=obj.course.id)).data

    def get_student(self, obj):
        return StudentSerializer(Student.objects.get(pk=obj.student.id)).data

    def get_dept(self, obj):
        return str(obj.dept.name)

    def get_session(self, obj):
        return str(obj.session.session)


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
