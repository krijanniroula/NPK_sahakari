from rest_framework import serializers
from .models import ShareMember, Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['provision','district','municipality','village','ward']

class ShareMemberSerializer(serializers.ModelSerializer):

    address = AddressSerializer(required=True)
    createdBy = serializers.ReadOnlyField(source='createdBy.username')
    class Meta:
        model = ShareMember
        fields = ['share_no','first_name', 'middle_name', 'last_name', 'email', 'phone', 'age', 'gender', 'father_name','address',
                  'mother_name', 'grand_father_name', 'alternative_person','amount_paid','extra_amount' ,'isActive','createdBy','createdAt', 'updatedAt']

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        share_member = ShareMember.objects.create(address=address,**validated_data)
        return share_member

    def update(self, instance, validated_data):
        address_serializer = self.fields['address']
        address_instance = instance.address

        address_data = validated_data.pop('address')
        address_serializer.update(address_instance,address_data)

        return super(ShareMemberSerializer, self).update(instance,validated_data)


