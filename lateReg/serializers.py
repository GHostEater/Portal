from rest_framework import serializers
from lateReg.models import RegStatus, LateReg, Log
from accounts.models import User, Student
from accounts.serializers import UserSerializer, StudentSerializer


class RegStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegStatus
        fields = "__all__"


class LateRegSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField()
    session = serializers.SerializerMethodField()

    class Meta:
        model = LateReg
        fields = "__all__"

    def get_student(self, obj):
        return StudentSerializer(Student.objects.get(pk=obj.student.id)).data

    def get_session(self, obj):
        return str(obj.session.session)


class LogSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField()
    approvedBy = serializers.SerializerMethodField()

    class Meta:
        model = Log
        fields = "__all__"

    def get_student(self, obj):
        return StudentSerializer(Student.objects.get(pk=obj.student.id)).data

    def get_approvedBy(self, obj):
        return UserSerializer(User.objects.get(pk=obj.approvedBy.id)).data
