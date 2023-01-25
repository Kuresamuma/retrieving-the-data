from django.shortcuts import render

# Create your views here.
from app.models import *

def display_Topics(request):
    QST=Topic.objects.all()
    d={'Topics':QST}
    return render(request,'display_Topics.html',d)


def display_Webpages(request):
    QSW=Webpage.objects.all()
    d={'Webpages':QSW}
    return render(request,'display_Webpages.html',d)

def display_AccessRecords(request):
    QSA=AccessRecords.objects.all()
    d={'AccessRecords':QSA}
    return render(request,'display_AccessRecords.html',d)