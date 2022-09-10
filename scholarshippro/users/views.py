
from django.shortcuts import render

# Create your views here.
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerializer

class CustomUserList(APIView):

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


        

class CustomUserDetail(APIView):
    
    def get_object(self,pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk):

        user = self.get_object(pk)
        if user == request.user:
            data = request.data
            serializer = CustomUserSerializer(
                instance=user,
                data=data,
                partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )
            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    def delete(self, request, pk):
        user = self.get_object(pk)
        if user == request.user:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            status=status.HTTP_401_UNAUTHORIZED
        )

class CustomUserDetailByEmail(APIView):
    
    def get_object(self, email):
        try:
            return CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            raise Http404
    
    def get(self, request, email):
        user = self.get_object(email)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
