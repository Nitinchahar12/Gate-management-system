"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from django.conf import settings
from EntryExit.views import Entry_Exit_view, output



urlpatterns = [
    path('admin/', admin.site.urls),
    path('entryexit/', Entry_Exit_view, name = 'entryexit'),
    path('output/<int:id>/', output, name='output'),

]
