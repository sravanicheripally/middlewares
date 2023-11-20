"""
URL configuration for middlewares_project project.

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
from app import views
from app import jwt_views

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('one',views.my_view),
    # path('users',views.user_info),
    path('/login_old', views.login_view, name='login'),
    path('home/', views.home_views, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('log/', views.log, name='log'),
    path('', jwt_views.login_view, name='login'),
    path('protected/', jwt_views.protected_view, name='protected'),
    path('refresh/', jwt_views.refresh_token_view, name='refresh'),
]
