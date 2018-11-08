from rest_framework import serializers

from paymentwaving.models import WavedPayment


class WavedPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WavedPayment
        fields = '__all__'
        depth = 5

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'payment_type',
            'student',
            'student__user',
            'student__major',
            'student__major__dept',
            'student__major__dept__college',
            'student__level',
            'student__mode_of_entry',
            'waved_by',
            'waved_by__user',
            'waved_by__dept',
            'waved_by__dept__college',
        )
        return queryset


class WavedPaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WavedPayment
        fields = '__all__'
