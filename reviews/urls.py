from django.urls import path
from . import views

urlpatterns = [
    path('', views.allreviews, name='reviews')
]