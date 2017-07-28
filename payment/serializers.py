from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from payment.models import Payment
from paymentType.models import PaymentType
from paymentType.serializers import PaymentTypeSerializer
from accounts.models import Student
from accounts.serializers import StudentSerializer


class PaymentSerializer(serializers.ModelSerializer):
    paymentType = serializers.SerializerMethodField()
    student = serializers.SerializerMethodField()
    session = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = '__all__'

    def get_paymentType(self, obj):
        return PaymentTypeSerializer(PaymentType.objects.get(pk=obj.paymentType.id)).data

    def get_student(self, obj):
        return StudentSerializer(Student.objects.get(pk=obj.student.id)).data

    def get_session(self, obj):
        return str(obj.session.session)


class PaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=Payment.objects.all(),
                fields=('student', 'paymentType', 'session')
            )
        ]
        model = Payment
        fields = '__all__'
