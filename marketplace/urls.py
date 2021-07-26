from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Produce, Profile


class ProfileView(APIView):
  def get(self, request):
    profiles = Profile.objects.all()
    return Response({"profiles": profiles})


class ProduceView(APIView):
  def get (self,request):
    produce=Produce.objects.all()
    return Response({"produce":produce})
    