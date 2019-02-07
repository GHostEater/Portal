from rest_framework import serializers
from sysinfo.models import SysInfo


class SysInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysInfo
        fields = "__all__"