"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from . import views
from login.views import welcome, login, logout, signup
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='home'),
    path('board/', views.board,name='board'),
	path('comment/', views.comment,name='comment'),
    path('edit/', views.edit ,name='edit'),
    url(r'^edit/(?P<mid>\w+?)/$', views.edit, name = 'edit'),

    url(r'^login/$',login,name='login'),
    url(r'^logout/$',logout,name='logout'),
    url(r'^welcome/$',welcome,name='welcome'),
    url(r'^signup/$',signup,name='signup'),
    
]
