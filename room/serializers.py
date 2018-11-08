from rest_framework import serializers
from room.models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        depth = 2

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'hostel',
        )
        return queryset


class RoomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
