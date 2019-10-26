from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ShareMember, Address
from rest_framework import status
from .serializers import ShareMemberSerializer, AddressSerializer

class ShareMemberList(APIView):
    def get(self, request, format=None):
        share_members = ShareMember.objects.all()
        serializer = ShareMemberSerializer(share_members, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        share_members = ShareMemberSerializer(data=request.data)
        if share_members.is_valid():
            share_members.save()
            return Response(share_members.data, status=status.HTTP_201_CREATED)
        return Response(share_members.errors, status=status.HTTP_400_BAD_REQUEST)

class ShareMemberDetail(APIView):
    def get_object(self, pk):
        try:
            return ShareMember.objects.get(pk=pk)
        except ShareMember.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        share_member = self.get_object(pk)
        serializer = ShareMemberSerializer(share_member)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        share_member = self.get_object(pk)
        serializer = ShareMemberSerializer(share_member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        share_member = self.get_object(pk)
        share_member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







