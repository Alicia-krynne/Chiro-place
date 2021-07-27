from django.db import models
from rest_framework import serializers


class ProduceSerializer(serializers.Serializer):
  produce_type =serializers.CharField(max_length=255)
  produce_description = serializers.CharField(max_length=255)
  produce_unit = serializers.CharField(max_length=2)
  produce_price =serializers.CharField(max_length=255)
  produce_location =serializers.CharField(max_length=255)





# class ProfileSerializer(serializers.Serializer):
#     profile_picture = CloudinaryField("profilepics",null= True)
#     name = models.CharField(max_length=255)
#     bio = models.CharField(max_length=1000)
#     profile_type = models.PositiveSmallIntegerField(choices=PROFILE_TYPE, blank=True, null=True)
#     Phone_number = models.EmailField()