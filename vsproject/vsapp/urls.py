from django.urls import path
from . import views

urlpatterns = [
    path('intro/',views.showIntro,name='intro'),
    # path('dashboard/',views.showDashboard,name='dashboard'),
    path("home/",views.showHome,name='home'),
    path("about/",views.showAbout,name='about'),
    path("contact/",views.showContact,name='contact'),
    path("crud/",views.showCrud,name='crud'),
    path("blog/",views.showBlog,name='blog'),
    path("register/",views.showRegister,name='register')
]
