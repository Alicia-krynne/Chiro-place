from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Produce, Profile
from .serializers import ProduceSerializer

class ProfileView(APIView):
  def get(self, request):
    profiles = Profile.objects.all()
    return Response({"profiles": profiles})


class ProduceView(APIView):
  def get (self,request):
    produce=Produce.objects.all()
    serializer = ProduceSerializer(produce, many=True)
    return Response({"produce": serializer.data})

