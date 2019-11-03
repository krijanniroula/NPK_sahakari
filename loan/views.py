from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from rest_framework import status
from .serializers import *


#Loan type
class LoanTypeList(APIView):
    def get(self, request, format=None):
        loan_type = LoanType.objects.all()
        serializer = LoanTypeSerializer(loan_type, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        loan_type = LoanTypeSerializer(data=request.data)
        if loan_type.is_valid():
            loan_type.save()
            return Response(loan_type.data, status=status.HTTP_201_CREATED)
        return Response(loan_type.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanTypeDetail(APIView):
    def get_object(self, slug):
        try:
            return LoanType.objects.get(slug=slug)
        except LoanType.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        loan_type = self.get_object(slug)
        serializer = LoanTypeSerializer(loan_type)
        return Response(serializer.data)

    def put(self, request, slug, format=None):
        loan_type = self.get_object(slug)
        serializer = LoanTypeSerializer(loan_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        loan_type = self.get_object(slug)
        loan_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#loan account
class LoanAccountList(APIView):
    def get(self, request, format=None):
        loan_account = LoanAccount.objects.all()
        serializer = LoanAccountSerializer(loan_account, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        loan_account = LoanAccountSerializer(data=request.data)
        if loan_account.is_valid():
            loan_account.save()
            return Response(loan_account.data, status=status.HTTP_201_CREATED)
        return Response(loan_account.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanAccountDetail(APIView):
    def get_object(self, pk):
        try:
            return LoanAccount.objects.get(pk=pk)
        except LoanAccount.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        loan_account = self.get_object(pk)
        serializer = LoanAccountSerializer(loan_account)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        loan_account = self.get_object(pk)
        serializer = LoanAccountSerializer(loan_account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        loan_account = self.get_object(pk)
        loan_account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Loan payment
class LoanPaymentList(APIView):
    def get(self, request, format=None):
        loan_payment = LoanPayment.objects.all()
        serializer = LoanPaymentSerializer(loan_payment, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        loan_payment = LoanPaymentSerializer(data=request.data)
        if loan_payment.is_valid():
            loan_payment.save()
            return Response(loan_payment.data, status=status.HTTP_201_CREATED)
        return Response(loan_payment.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanPaymentDetail(APIView):
    def get_object(self, pk):
        try:
            return LoanPayment.objects.get(pk=pk)
        except LoanPayment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        loan_payment = self.get_object(pk)
        serializer = LoanPaymentSerializer(loan_payment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        loan_payment = self.get_object(pk)
        serializer = LoanPaymentSerializer(loan_payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        loan_payment = self.get_object(pk)
        loan_payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Loan payment History
class LoanPaymentHistoryList(APIView):
    def get(self, request, format=None):
        loan_payment_history = LoanPaymentHistory.objects.all()
        serializer = LoanPaymentHistorySerializer(loan_payment_history, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     loan_payment_history = LoanPaymentHistorySerializer(data=request.data)
    #     if loan_payment_history.is_valid():
    #         loan_payment_history.save()
    #         return Response(loan_payment_history.data, status=status.HTTP_201_CREATED)
    #     return Response(loan_payment_history.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanPaymentHistoryDetail(APIView):
    def get_object(self, pk):
        try:
            return LoanPaymentHistory.objects.get(pk=pk)
        except LoanPaymentHistory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        loan_payment_history = self.get_object(pk)
        serializer = LoanPaymentHistorySerializer(loan_payment_history)
        return Response(serializer.data)

    # def put(self, request, pk, format=None):
    #     loan_payment_history = self.get_object(pk)
    #     serializer = LoanPaymentHistorySerializer(loan_payment_history, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk, format=None):
    #     loan_payment_history = self.get_object(pk)
    #     loan_payment_history.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)






