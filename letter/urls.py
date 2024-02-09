
from django.urls import path

from . import views

urlpatterns = [
    path('', views.letter, name='letters'),
    path('newLetter', views.newLetter, name="newLetter")
] 