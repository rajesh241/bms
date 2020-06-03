from django.urls import path, include, re_path
from rest_framework import routers
from baseapp import views
app_name = 'baseapp'
urlpatterns = [
    path('exotel/passthru', views.ExotelView.as_view(), name='entity')
]
