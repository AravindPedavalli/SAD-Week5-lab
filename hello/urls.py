from django.urls import path
from . import views

urlpatterns = [
    path('json/', views.hello_world_json),
    path('', views.hello_world_json),
]
