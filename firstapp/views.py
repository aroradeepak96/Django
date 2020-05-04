from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LoginSerializer
from .models import Login
from .import models
from .import serializers

def index(request):
    return render(request,'FirstApp/index.html')
def training_domain(request,domain_id):
    return HttpResponse("You are in the %s:" % domain_id)
def candidate(request,domain_id):
    response="you are the candiate named as %s"
    return HttpResponse(response  % domain_id) 
def login(request):
    return render(request,'firstapp/login.html')
class LoginList(APIView):
    def get(self,request):
        values=Login.objects.all()
        Serializer=LoginSerializer(values,many=True)
        return Response(Serializer.data)
        
class LoginViewset(viewsets.ModelViewSet):
    queryset = models.Login.objects.all()
    serializer_class=serializers.LoginSerializer
    
class pythonViewset(viewsets.ModelViewSet):
    queryset = models.python.objects.all()
    serializer_class=serializers.pythonSerializer
    
class studentViewset(viewsets.ModelViewSet):
    queryset = models.student.objects.all()
    serializer_class=serializers.studentSerializer
    
def random(request):
    data={1:{'name':'Deepak','age':25},2:{'name':'rahul','age':25}}
    return JsonResponse(data)
    

