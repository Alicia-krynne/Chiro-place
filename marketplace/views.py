from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Produce, Profile
from .serializers import ProduceSerializer,ProfileSerializer
from django.shortcuts import render ,redirect
from django.http.response import Http404
from rest_framework import serializers,status
from .permissions import IsAdminOrReadOnly

class ProfileView(APIView):
  def get_profile(self , pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

  def get(self, request):
    profile=Profile.objects.all()
    serializer = ProfileSerializer(profile, many=True)
    return Response({"profile": serializer.data})
  
  def post(self,request,format=None):
        permission_classes = (IsAdminOrReadOnly,)
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data , status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class ProduceView(APIView):
  def get_produce(self , pk):
        try:
            return Produce.objects.get(pk=pk)
        except Produce.DoesNotExist:
            return Http404
  
  def get (self,request):
    produce=Produce.objects.all()
    serializer = ProduceSerializer(produce, many=True)
    return Response({"produce": serializer.data})
  
  def post(self,request,format=None):
        permission_classes = (IsAdminOrReadOnly,)
        serializers = ProduceSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data , status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

  def put(self , request ,pk, format= None):
        permission_classes = (IsAdminOrReadOnly,)
        produce = self.get_produce(pk)
        serializers = ProduceSerializer(produce , request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors , status=status.HTTP_400_BAD_REQUEST)

  def delete(self , request , pk,format= None):
        permission_classes = (IsAdminOrReadOnly,)
        produce=self.get_produce(pk)
        produce.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
