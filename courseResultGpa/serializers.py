from rest_framework import serializers
from courseResultGpa.models import CourseResultGPA
from accounts.models import Student
from accounts.serializers import StudentSerializer


class CourseResultGPASerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField()
    session = serializers.SerializerMethodField()
    dept = serializers.SerializerMethodField()
    deptId = serializers.CharField(read_only=True)

    class Meta:
        model = CourseResultGPA
        fields = '__all__'

    def get_student(self, obj):
        return StudentSerializer(Student.objects.get(pk=obj.student.id)).data

    def get_session(self, obj):
        return str(obj.session.session)

    def get_dept(self, obj):
        return str(obj.dept.name)

    def get_deptId(self, obj):
        return str(obj.dept.id)
