from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),  # This is an endpoint
    # As this endpoint adds data, note the url path
    path('add/', views.postData),
]