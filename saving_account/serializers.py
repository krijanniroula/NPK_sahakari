from rest_framework import serializers
from .models import *
from share_member.models import ShareMember
from share_member.serializers import ShareMemberSerializer

class SavingTypeSerializer(serializers.ModelSerializer):
    createdBy = serializers.ReadOnlyField(source='createdBy.username')
    slug = serializers.ReadOnlyField()
    class Meta:
        model = SavingType
        fields = ['name','account_type','interest_rate', 'slug','createdBy', 'createdAt', 'updatedAt']

        def create(self, validated_data):
            saving_type = SavingType.objects.create( **validated_data)
            return saving_type

        def update(self, instance, validated_data):
            return super(SavingTypeSerializer, self).update(instance, validated_data)

class SavingAccountSerializer(serializers.ModelSerializer):
    saving_type = SavingTypeSerializer(read_only=True)
    saving_type_id = serializers.PrimaryKeyRelatedField(source='saving_type',  queryset=SavingType.objects.all() )

    share_member = ShareMemberSerializer(read_only=True)
    share_member_id = serializers.PrimaryKeyRelatedField(source='share_member', queryset=ShareMember.objects.all())
    createdBy = serializers.ReadOnlyField(source='createdBy.username')
    class Meta:
        model = SavingAccount
        fields = ['account_number','share_member_id','share_member','saving_type_id','saving_type', 'time_in_yr', 'createdBy', 'createdAt', 'updatedAt']

    def create(self, validated_data):
        saving_account= SavingAccount.objects.create(**validated_data)
        return saving_account

    def update(self, instance, validated_data):
        return super(SavingAccountSerializer, self).update(instance,validated_data)


class SavingSerializer(serializers.ModelSerializer):
    saving_account = SavingAccountSerializer(read_only=True)
    saving_account_id = serializers.PrimaryKeyRelatedField(source='saving_account', queryset=SavingAccount.objects.all())
    createdBy = serializers.ReadOnlyField(source='createdBy.username')
    class Meta:
        model = Saving
        fields = ['saving_account','saving_account_id','particular','amount','amount_type','createdBy', 'createdAt', 'updatedAt']

    def create(self, validated_data):
        saving= Saving.objects.create(**validated_data)
        return saving

    def update(self, instance, validated_data):
        return super(SavingSerializer, self).update(instance,validated_data)

