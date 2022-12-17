from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse
from main.models import *

## Create your views here.
def main(request):
    return render(request, 'base_generic.html')
    # primjetiti korištenje HTML-a

class MjestoList(ListView):
    model=Mjesto

class SveucilisteList(ListView):
    model=Sveuciliste

class SrednjaList(ListView):
    model=SrednjaSkola

class FakultetList(ListView):
    model=Fakultet            

class SmjerList(ListView):
    model=Smjer
  

class MaturantList(ListView):
    model=Maturant

class StudentList(ListView):
    model=Student

