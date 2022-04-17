"""Quicboar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path
from django.views.static import serve
from .settings import STATIC_ROOT
from Quicboar import views
from django.conf.urls import handler400, handler403, handler404, handler500

urlpatterns = [
    re_path('^static/(?P<path>.*)', serve, {'document_root': STATIC_ROOT}),
    # path('admin/', admin.site.urls),
    path('',views.index),
    path('index/',views.index),
# path('index-2/',views.index2),
# path('index-3/',views.index3),
path('courses/',views.courses),
path('contact/',views.contact),
path('aboutus/',views.aboutus),
path('instructor/',views.instructor),
]
handler400 = views.bad_request
handler403 = views.permission_denied
handler404 = views.page_not_found
handler500 = views.server_error