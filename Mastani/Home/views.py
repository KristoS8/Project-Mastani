from django.shortcuts import render
from .models import literasi
# Create your views here.

def index(request):
    return render (request, "Home/index.html", {'active_page': 'home'})

def literasi_view(request):
    data_literasi = literasi.objects.all()
    context = {
        'data_literasi':data_literasi,
        'active_page':'literasi'
    }
    
    return render (request, 'Home/literasi.html', context)

def keuangan_view(request):
    return render (request, "Home/keuangan.html", {'active_page':'keuangan'})

def pemasaran_view(request):
    return render (request, "Home/pemasaran.html", {'active_page':'pemasaran'})

def about_view(request):
    return render (request, "Home/about.html", {'active_page':'about'})