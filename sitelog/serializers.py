from rest_framework import serializers
from sitelog.models import Log


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = "__all__"
