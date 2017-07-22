from rest_framework import serializers
from levelAdviser.models import LevelAdviser

from accounts.models import Lecturer
from accounts.serializers import LecturerSerializer


class LevelAdviserSerializer(serializers.ModelSerializer):
    lecturer = serializers.SerializerMethodField()
    major = serializers.SerializerMethodField()

    class Meta:
        model = LevelAdviser
        fields = '__all__'

    def get_lecturer(self, obj):
        lecturer = Lecturer.objects.get(pk=obj.lecturer.id)
        lecturer_s = LecturerSerializer(lecturer).data
        return lecturer_s

    def get_major(self, obj):
        return str(obj.major.name)

    def get_level(self, obj):
        return str(obj.level.level)
