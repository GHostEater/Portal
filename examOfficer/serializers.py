from rest_framework import serializers

from examOfficer.models import ExamOfficer
from accounts.models import Lecturer
from accounts.serializers import LecturerSerializer


class ExamOfficerSerializer(serializers.ModelSerializer):
    lecturer = serializers.SerializerMethodField()
    dept = serializers.SerializerMethodField()
    deptId = serializers.SerializerMethodField()

    class Meta:
        model = ExamOfficer
        fields = '__all__'

    def get_lecturer(self, obj):
        return LecturerSerializer(Lecturer.objects.get(pk=obj.lecturer.id)).data

    def get_dept(self, obj):
        return str(obj.dept.name)

    def get_deptId(self, obj):
        return str(obj.dept.id)
