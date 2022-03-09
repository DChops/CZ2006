from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('get/', views.getData),  # This is an endpoint
    # As this endpoint adds data, note the url path
    path('post/', views.postData),
]