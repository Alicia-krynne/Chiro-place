from django import forms
from .models import Comment, Produce,Profile

class NewProduceForm(forms.ModelForm):
    class Meta:
      model = Produce
      fields = [' produce_image','produce_type','produce_description','produce_unit','produce_price','produce_location']
        

class CommentForm(forms.ModelForm):
   class Meta:
        model = Comment
        exclude = ['user']
