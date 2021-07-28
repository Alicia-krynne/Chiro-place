from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Profile(models.Model):
  PROFILE_TYPE=(
  ('FARMER', 'Farmer'),
  ('CONSUMER','Consumer'),
  )   
  photo_url = CloudinaryField("profilepics",null= True)
  name = models.CharField(max_length=255)
  bio = models.CharField(max_length=1000)
  profile_type = models.CharField(max_length=255,choices=PROFILE_TYPE )
  Phone_number = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class Produce(models.Model):
  PRODUCE_UNIT = (
        ('LT', 'Litres'),
        ('KG', 'Kilograms'),
        ('C', 'Crates'),
        ('E', 'Each'),
    )
  produce_image = CloudinaryField("produce_images",null= True)
  produce_type =models.CharField(max_length=255)
  produce_description = models.CharField(max_length=255)
  produce_unit = models.CharField(max_length=2, choices=PRODUCE_UNIT)
  produce_price =models.IntegerField()
  produce_location =models.CharField(max_length=255)

  def __str__(self):
    return self.produce_type

class Comment(models.Model):
    post = models.ForeignKey(Produce,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


  
