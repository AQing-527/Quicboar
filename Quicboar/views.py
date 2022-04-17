import re

from django.http import HttpResponse

# from . import models
# Create your views here.
from django.shortcuts import render,redirect


def bad_request(request, exception, template_name='400.html'):
    return render(request, template_name)


def permission_denied(request, exception, template_name='403.html'):
    return render(request, template_name)


def page_not_found(request, exception, template_name='404.html'):
    return render(request, template_name)


def server_error(request, template_name='500.html'):
    return render(request, template_name)


def index(request):

    return render(request,'index.html',locals())


def courses(request):
    return render(request,'course.html',locals())


def contact(request):
    return render(request,'contact.html',locals())


def aboutus(request):
    return render(request,'about-1.html',locals())


def instructor(request):
    return render(request,'instructor.html',locals())