from django.contrib import admin
from django.urls import path
from homepage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup, name = 'signup'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('logout', views.logout, name = 'logout'),
    path('home', views.home, name = 'home'),
]