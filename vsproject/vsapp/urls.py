from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('intro/',views.showIntro,name='intro'),
    # path('dashboard/',views.showDashboard,name='dashboard'),
    path("home/",views.showHome,name='home'),
    path("about/",views.showAbout,name='about'),
    path("contact/",views.showContact,name='contact'),
    path("crud/",views.showCrud,name='crud'),
    path("blog/",views.showBlog,name='blog'),
    path("register/",views.showRegister,name='register'),
    path("login/",LoginView.as_view(template_name='login.html'),name='login'),
]
