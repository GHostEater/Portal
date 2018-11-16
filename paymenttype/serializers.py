from rest_framework import serializers
from paymenttype.models import PaymentType, TuitionFee


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = '__all__'
        
        
class TuitionFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TuitionFee
        fields = '__all__'
