from marketplace.models import Profile
from django.db import models
from rest_framework import serializers


class ProduceSerializer(serializers.Serializer):
  produce_type =serializers.CharField(max_length=255,default='Farmer')
  produce_description = serializers.CharField(max_length=255)
  produce_unit = serializers.CharField(max_length=2)
  produce_price =serializers.CharField(max_length=255)
  produce_location =serializers.CharField(max_length=255)
  Produce_image = serializers.ImageField()



class ProfileSerializer(serializers.Serializer):
  photo_url = serializers.SerializerMethodField()
  class Meta:
      model = Profile
      fields = ('id','name','bio','photo_url','phone_number','profile_type') 
  def get_profile_picture(self, profile):
      request = self.context.get('request')
      photo_url = profile.photo.url
      return request.build_absolute_uri(photo_url)

