from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets


class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


