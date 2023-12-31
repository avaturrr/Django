"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from app1.views import get_data, number_2, even_number, save_name, full_form

urlpatterns = [
    path("", get_data, name="home_page"),
    path("number/<int:number>", number_2),
    path("my_word/<str:word>", even_number, name="even_number"),
    path("save_name", save_name, name="save_name"),
    path("full_form", full_form, name="full_form"),
]
