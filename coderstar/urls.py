from django.urls import path
from coderstar import views

urlpatterns = [
    path('home/',views.greetings),
    path('home/run/',views.runcode),
]
