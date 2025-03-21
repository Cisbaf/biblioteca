"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from app import views
from social_django import urls as social_urls


urlpatterns = [
    path('admin/', admin.site.urls, name='painel'),
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('register', views.register, name="register"),
    path('sobre', views.sobre, name="sobre"),
    path('auth-login', views.auth_login, name="auth_login"),
    path('auth-register', views.auth_register, name="auth_register"),
    path('auth/', include(social_urls)),
    path('book/', include("book.urls")),
    path('rental/', include("rental.urls")),
    path('ticket/', include("ticket.urls"))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
