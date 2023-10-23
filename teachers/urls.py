from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.say_welcome),
    path('about/', views.about),
    path('timetable/', views.timetable),
    path('notice/', views.note)
]
