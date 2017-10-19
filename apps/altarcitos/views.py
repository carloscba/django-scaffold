from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from . import models
from . import serializers
from . import permissions


class AltarcitosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AltarcitosSerializer
    queryset = models.Altarcitos.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('uid',)
