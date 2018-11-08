from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from roomallocation.models import RoomAllocation


class RoomAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomAllocation
        fields = '__all__'
        depth = 4

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'student',
            'student__user',
            'student__major',
            'student__major__dept',
            'student__major__dept__college',
            'student__level',
            'student__mode_of_entry',
            'room',
            'session',
            'allocated_by',
            'allocated_by__user',
        )
        return queryset


class RoomAllocationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=RoomAllocation.objects.all(),
                fields=('student', 'session')
            )
        ]
        model = RoomAllocation
        fields = '__all__'
