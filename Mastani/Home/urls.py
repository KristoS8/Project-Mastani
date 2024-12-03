from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('literasi/', views.literasi_view, name='literasi'),
    path('pembeli/keuangan/', views.keuangan_view, name="keuangan"),
    path('pembeli/pemasaran/', views.pemasaran_view, name="pemasaran"),
    path('about/', views.about_view, name='about')
]