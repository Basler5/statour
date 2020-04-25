from django.urls import path
from . import views


urlpatterns = [
    path('', views.search, name='search'),
    path('rezult/', views.rezult, name='rezult'),
    path('tech/', views.tech, name='tech'),
]