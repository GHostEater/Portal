from rest_framework import serializers

from courseResultEditRequest.models import Request, Log
from accounts.models import User, Lecturer
from accounts.serializers import UserSerializer, LecturerSerializer


class RequestSerializer(serializers.ModelSerializer):
    lecturer = serializers.SerializerMethodField()
    handledBy = serializers.SerializerMethodField()

    class Meta:
        model = Request
        fields = '__all__'

    def get_lecturer(self, obj):
        return LecturerSerializer(Lecturer.objects.get(pk=obj.lecturer.id)).data

    def get_handledBy(self, obj):
        return UserSerializer(User.objects.get(pk=obj.handledBy.user.id)).data


class LogSerializer(serializers.ModelSerializer):
    editedBy = serializers.SerializerMethodField()

    class Meta:
        model = Log
        fields = '__all__'

    def get_editedBy(self, obj):
        return LecturerSerializer(Lecturer.objects.get(pk=obj.editedBy.id)).data
