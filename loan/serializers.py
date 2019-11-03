from rest_framework import serializers
from .models import *
from share_member.models import ShareMember
from share_member.serializers import ShareMemberSerializer

class LoanTypeSerializer(serializers.ModelSerializer):
    createdBy = serializers.ReadOnlyField(source='createdBy.username')
    slug = serializers.ReadOnlyField()
    class Meta:
        model = LoanType
        fields = ['name','interest_rate','slug','createdBy','createdAt','updatedAt']

        def create(self, validated_data):
            loan_type = LoanType.objects.create( **validated_data)
            return loan_type

        def update(self, instance, validated_data):
            return super(LoanTypeSerializer, self).update(instance, validated_data)

class LoanAccountSerializer(serializers.ModelSerializer):
    loan_type = LoanTypeSerializer(read_only=True)
    loan_type_id = serializers.PrimaryKeyRelatedField(source='loan_type',  queryset=LoanType.objects.all() )

    share_member = ShareMemberSerializer(read_only=True)
    share_member_id = serializers.PrimaryKeyRelatedField(source='share_member', queryset=ShareMember.objects.all())
    createdBy = serializers.ReadOnlyField(source='createdBy.username')
    class Meta:
        model = LoanAccount
        fields = ['loan_number','share_member_id','share_member','loan_type_id','loan_type', 'status','amount_received' ,'createdBy', 'createdAt', 'updatedAt']

    def create(self, validated_data):
        saving_account= LoanAccount.objects.create(**validated_data)
        return saving_account

    def update(self, instance, validated_data):
        return super(LoanAccountSerializer, self).update(instance,validated_data)


class LoanPaymentSerializer(serializers.ModelSerializer):
    loan_account = LoanAccountSerializer(read_only=True)
    loan_account_id = serializers.PrimaryKeyRelatedField(source='loan_account', queryset=LoanAccount.objects.all())
    createdBy = serializers.ReadOnlyField(source='createdBy.username')
    class Meta:
        model = LoanPayment
        fields = ['id','loan_account','loan_account_id','paid','createdBy', 'createdAt', 'updatedAt']

    def create(self, validated_data):
        saving= LoanPayment.objects.create(**validated_data)
        return saving

    def update(self, instance, validated_data):
        return super(LoanPaymentSerializer, self).update(instance,validated_data)

class LoanPaymentHistorySerializer(serializers.ModelSerializer):
    loan_payment = LoanPaymentSerializer(read_only=True)
    loan_payment_id = serializers.PrimaryKeyRelatedField(source='loan_payment', queryset=LoanPayment.objects.all())
    createdBy = serializers.ReadOnlyField(source='createdBy.username')


    class Meta:
        model = LoanPaymentHistory
        fields = ['id','loan_payment','loan_payment_id','date','principle','interest','paid','remaining','createdBy', 'createdAt', 'updatedAt']

    def create(self, validated_data):
        saving= LoanPaymentHistory.objects.create(**validated_data)
        return saving

    def update(self, instance, validated_data):
        return super(LoanPaymentHistorySerializer, self).update(instance,validated_data)





