from rest_framework import serializers
from modeOfEntry.models import ModeOfEntry


class ModeOfEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeOfEntry
        fields = [
            'id',
            'name',
        ]
