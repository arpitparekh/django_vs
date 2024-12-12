from django.urls import path
from . import views

urlpatterns = [
    path('intro/',views.showIntro,name='intro'),
]
