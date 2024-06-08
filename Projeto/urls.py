from django.urls import path, include
from app_Projeto import views

urlpatterns = [
    path('', views.index,name='index'),
    path('', include('app_Projeto.urls')),
]
