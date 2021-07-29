from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Produce, Profile
from .serializers import ProduceSerializer,ProfileSerializer
from django.shortcuts import render ,redirect
from django.http.response import Http404
from rest_framework import serializers,status
from .permissions import IsAdminOrReadOnly
from .forms import NewProduceForm

def welcome(request):
    profile=Profile.objects.all()
    produce= Produce.objects.all()
    
    return render(request,"homepage.html",{"profile":profile,"produce":produce})

def search_results(request):
    
  if 'produce' in request.GET and request.GET["produce"]:
        search_term = request.GET.get("produce")
        searched_produce = Produce.search_by_produce_type(search_term)
        message = f"{search_term}"

        return render(request, "search.html",{"message":message,"project": searched_produce})
  
  else:
    message="No search made"
    return render(request,"search.html",{"message":message})

def display_all_produce(request):
    try:
        produce = Produce.objects.all()
        print(produce)
        return render(request,"produce.html", {"produce":produce})

    except Produce.DoesNotExist:
        raise Http404()
    

def sell(request):
    produce = Produce.objects.all()
    current_user = request.user
    if request.method == 'POST':
        form = NewProduceForm(request.POST, request.FILES)
        if form.is_valid():
            produce= form.save(commit=False)
            produce.user = current_user
            produce.save()
        return redirect('/')

    else:
        form = NewProduceForm()
    return render(request, 'sell.html', {"form": form,"produce":produce })

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
