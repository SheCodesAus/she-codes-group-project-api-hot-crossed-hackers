from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Scholarships
from.serializers import ScholarshipSerializer, ScholarshipDetailSerializer
from django.http import Http404
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly

class ScholarshipsList(APIView):

    def get(self, request):
            scholarship = Scholarships.objects.all()
            serializer = ScholarshipSerializer(scholarship, many=True)
            return Response(
                serializer.data)
                

    def post(self, request):
        serializer = ScholarshipSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data,
            status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



class ScholarshipDetail(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            scholarship = Scholarships.objects.get(pk=pk)
            self.check_object_permissions(self.request, scholarship)
            return scholarship
        except Scholarships.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        scholarship = self.get_object(pk)
        serializer = ScholarshipSerializer(scholarship)
        return Response(serializer.data)

    def put(self, request, pk):
        scholarship = self.get_object(pk)
        data = request.data
        serializer = ScholarshipDetailSerializer(
            instance=scholarship, 
            data=data, 
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
        
