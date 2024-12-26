from django.urls import path
from . import views

urlpatterns = [
    path('intro/',views.showIntro,name='intro'),
    # path('dashboard/',views.showDashboard,name='dashboard'),
    path("home/",views.showHome,name='home')
]
