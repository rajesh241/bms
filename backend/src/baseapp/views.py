from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from django.http import HttpResponse
from rest_framework import (generics, authentication, permissions,
                            status, mixins, exceptions)

# Create your views here.



class ExotelView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, *args, **kwargs):
        print(request.query_params)
        return HttpResponse({'message': 'Thanks'}, status=200)
