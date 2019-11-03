from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from rest_framework import status
from .serializers import *


#savingtype
class SavingTypeList(APIView):
    def get(self, request, format=None):
        saving_type = SavingType.objects.all()
        serializer = SavingTypeSerializer(saving_type, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        saving_type = SavingTypeSerializer(data=request.data)
        if saving_type.is_valid():
            saving_type.save()
            return Response(saving_type.data, status=status.HTTP_201_CREATED)
        return Response(saving_type.errors, status=status.HTTP_400_BAD_REQUEST)

class SavingTypeDetail(APIView):
    def get_object(self, slug):
        try:
            return SavingType.objects.get(slug=slug)
        except SavingType.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        saving_type = self.get_object(slug)
        serializer = SavingTypeSerializer(saving_type)
        return Response(serializer.data)

    def put(self, request, slug, format=None):
        saving_type = self.get_object(slug)
        serializer = SavingTypeSerializer(saving_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        saving_type = self.get_object(slug)
        saving_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#savingaccount
class SavingAccountList(APIView):
    def get(self, request, format=None):
        saving_account = SavingAccount.objects.all()
        serializer = SavingAccountSerializer(saving_account, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        saving_account = SavingAccountSerializer(data=request.data)
        if saving_account.is_valid():
            saving_account.save()
            return Response(saving_account.data, status=status.HTTP_201_CREATED)
        return Response(saving_account.errors, status=status.HTTP_400_BAD_REQUEST)

class SavingAccountDetail(APIView):
    def get_object(self, pk):
        try:
            return SavingAccount.objects.get(pk=pk)
        except SavingAccount.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        saving_account = self.get_object(pk)
        serializer = SavingAccountSerializer(saving_account)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        saving_account = self.get_object(pk)
        serializer = SavingAccountSerializer(saving_account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        saving_account = self.get_object(pk)
        saving_account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#saving
class SavingList(APIView):
    def get(self, request, format=None):
        saving = Saving.objects.all()
        serializer = SavingSerializer(saving, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        saving = SavingSerializer(data=request.data)
        if saving.is_valid():
            saving.save()
            return Response(saving.data, status=status.HTTP_201_CREATED)
        return Response(saving.errors, status=status.HTTP_400_BAD_REQUEST)

class SavingDetail(APIView):
    def get_object(self, pk):
        try:
            return Saving.objects.get(pk=pk)
        except Saving.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        saving = self.get_object(pk)
        serializer = SavingSerializer(saving)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        saving = self.get_object(pk)
        serializer = SavingSerializer(saving, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        saving = self.get_object(pk)
        saving.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






