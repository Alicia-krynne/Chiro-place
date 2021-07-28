from marketplace.models import Produce, Profile
from django.db import models
from rest_framework import serializers


class ProduceSerializer(serializers.Serializer):
  produce_image = serializers.URLField()
  class Meta:
      model = Produce
      fields = ('id','produce_type','produce description','produce_unit','produce_price','produce_location','produce_image') 
  
  def get_product_image(self, profile):
      request = self.context.get('request')
      produce_image = profile.photo.url
      return request.build_absolute_uri(produce_image)

  
  produce_type =serializers.CharField(max_length=255,default='Farmer')
  produce_description = serializers.CharField(max_length=255)
  produce_unit = serializers.CharField(max_length=2)
  produce_price =serializers.CharField(max_length=255)
  produce_location =serializers.CharField(max_length=255)
  

class ProfileSerializer(serializers.Serializer):
  photo_url = serializers.URLField()
  class Meta:
      model = Profile
      fields = ('id','name','bio','photo_url','phone_number','profile_type') 

  name = serializers.CharField(max_length=255)
  about = serializers.CharField(max_length=1000)
  profile_type = serializers.CharField(max_length=255,default='each')
  Phone_number = serializers.CharField(max_length=255)   
  
  def get_profile_picture(self, profile):
      request = self.context.get('request')
      photo_url = profile.photo.url
      return request.build_absolute_uri(photo_url)

