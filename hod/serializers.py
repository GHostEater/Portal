from rest_framework import serializers

from accounts.serializers import LecturerSerializer
from accounts.models import Lecturer
from hod.models import Hod


class HodSerializer(serializers.ModelSerializer):
    lecturer = serializers.SerializerMethodField()
    dept = serializers.SerializerMethodField()

    class Meta:
        model = Hod
        fields = [
            'lecturer',
            'dept'
        ]

    def get_lecturer(self, obj):
        lecturer = Lecturer.objects.get(pk=obj.lecturer.id)
        lecturer_s = LecturerSerializer(lecturer).data
        return lecturer_s

    def get_dept(self, obj):
        return str(obj.dept.name)
