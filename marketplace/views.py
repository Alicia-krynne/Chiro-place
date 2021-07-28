from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Produce, Profile
from .serializers import ProduceSerializer,ProfileSerializer

class ProfileView(APIView):
  def get(self, request):
    profile=Profile.objects.all()
    serializer = ProfileSerializer(profile, many=True)
    return Response({"profile": serializer.data})

class ProduceView(APIView):
  def get (self,request):
    produce=Produce.objects.all()
    serializer = ProduceSerializer(produce, many=True)
    return Response({"produce": serializer.data})

