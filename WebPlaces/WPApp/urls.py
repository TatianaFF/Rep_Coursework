"""WebPlaces URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from WPApp import views

urlpatterns = [
    path('', views.mainFunc, name='main'),
    path('<int:place_id>/', views.detail, name='detail'),
    path('<int:place_id>/add_comment/', views.add_comment, name='add_comment'),
    path('<int:place_id>/add_favorite/', views.add_favorite, name='add_favorite'),
    path('<int:place_id>/remove_favorite/', views.remove_favorite, name='remove_favorite'),
    path('place/', views.CreatePlace.as_view(), name='place'),
    path('account/', views.account, name='account'),
    path('about_us/', views.about_us),
    path('register/', views.RegisterFormView.as_view(), name='register'),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
