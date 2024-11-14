from django.urls import path
from profilee import views

urlpatterns = [
    path('', views.home, name='home'),
]