from rest_framework import serializers
from nysc.models import Nysc


class NyscSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nysc
        fields = '__all__'
