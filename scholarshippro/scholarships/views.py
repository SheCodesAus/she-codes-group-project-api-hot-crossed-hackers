from unicodedata import category
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Scholarships
from.serializers import ScholarshipSerializer, ScholarshipDetailSerializer
from django.http import Http404
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404

class ScholarshipsList(APIView):

    def get(self, request):
            categories = request.query_params
            if len(categories) == 0:
                scholarship = Scholarships.objects.all()
            else:
                gender = categories.get('gender', Scholarships.Gender.ANY)
                indigenous_status = categories.get('indigenous_status', Scholarships.IndigenousStatus.ANY)
                vision_impairment = categories.get('vision_impairment', Scholarships.VisionImpairment.ANY)
                low_income = categories.get('low_income', Scholarships.LowIncome.ANY)
                esol = categories.get('esol', Scholarships.ESOL.ANY)
                duration = categories.get('duration', Scholarships.Duration.ANY)
                scholarship = Scholarships.objects.filter(
                    gender__in=[Scholarships.Gender.ANY, gender],
                    indigenous_status__in=[Scholarships.IndigenousStatus.ANY, indigenous_status],
                    vision_impairment__in=[Scholarships.VisionImpairment.ANY, vision_impairment],
                    low_income__in=[Scholarships.LowIncome.ANY, low_income],
                    esol__in=[Scholarships.ESOL.ANY, esol],
                    duration__in=[Scholarships.Duration.ANY, duration]
                )
            serializer = ScholarshipSerializer(scholarship, many=True)
            return Response(
                serializer.data
            )
                

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
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        scholarship = Scholarships.objects.get(pk=pk)
        if scholarship.owner == request.user:
            scholarship.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            status=status.HTTP_401_UNAUTHORIZED
        )

class FavoriteDetail(APIView):

    def get_object(self, pk):
        try:
            scholarship = Scholarships.objects.get(pk=pk)
            return scholarship
        except Scholarships.DoesNotExist:
            raise Http404

    def post(self, request, pk):
        scholarship = self.get_object(pk)
        
        if request.user not in scholarship.favorites.all():
            scholarship.favorites.add(request.user)
            return Response(
            status=status.HTTP_201_CREATED
            )
        return Response(
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        scholarship = Scholarships.objects.get(pk=pk)
        
        if request.user in scholarship.favorites.all():
            scholarship.favorites.remove(request.user)
            return Response(
            status=status.HTTP_204_NO_CONTENT
            )
        return Response(
            status=status.HTTP_400_BAD_REQUEST
        )


        

