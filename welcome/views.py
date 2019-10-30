import os
import uuid
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView, Mission

# Create your views here.

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    m1 = Mission()
    m1.save()
    m1.is_deleted = True
    m1.save()

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    return HttpResponse(PageView.objects.count())
