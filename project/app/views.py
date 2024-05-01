from django.shortcuts import render
from rest_framework import viewsets
from .serializers import*
from .models import *
from rest_framework.permissions import IsAuthenticated,IsAdminUser

# Create your views here.


class MovieViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAuthenticated]
	queryset = Movies.objects.all()
	serializer_class = Movieserializer

class StudentViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAdminUser]
	queryset = Student.objects.all()
	serializer_class = Studentserializer