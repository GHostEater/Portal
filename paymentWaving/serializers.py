from rest_framework import serializers

from paymentType.serializers import PaymentTypeSerializer
from accounts.serializers import StudentSerializer, LecturerSerializer

from paymentWaving.models import WavedPayment
from paymentType.models import PaymentType
from accounts.models import Student, Lecturer


class WavedPaymentSerializer(serializers.ModelSerializer):
    paymentType = serializers.SerializerMethodField()
    student = serializers.SerializerMethodField()
    wavedBy = serializers.SerializerMethodField()

    class Meta:
        model = WavedPayment
        fields = '__all__'

    def get_paymentType(self, obj):
        return PaymentTypeSerializer(PaymentType.objects.get(pk=obj.paymentType.id)).data

    def get_student(self, obj):
        return StudentSerializer(Student.objects.get(pk=obj.student.id)).data

    def get_wavedBy(self, obj):
        return LecturerSerializer(Lecturer.objects.get(pk=obj.wavedBy.id)).data


class WavedPaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WavedPayment
        fields = '__all__'
