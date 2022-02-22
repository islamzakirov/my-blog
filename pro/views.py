from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authentication import BaseAuthentication
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class BlogViewSet(viewsets.ModelViewSet):
   queryset = Blog.objects.all()
   serializer_class = BlogSerializer 
   filterset_field = ['name']
   filter_backends = [filters.OrderingFilter, DjangoFilterBackend,filters.SearchFilter]
   ordering_fields = ['name']
   ordering = ['name']
   search_fields = ['name']
#    permission_classes = [IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer