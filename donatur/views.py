from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Donatur
from pembayaran.models import Donasi
from .forms import DonaturForm
from pembayaran.forms import DonasiForm

# Create your views here.

class DonaturListView(ListView):
    model = Donatur
    context_object_name = 'donatur'

class DonasiListView(ListView):
    model = Donasi
    context_object_name = 'donasi'

class DonaturCreateView(CreateView):
    model = Donatur
    form_class = DonaturForm
    success_url = reverse_lazy('donatur:donatur_list')

class DonasiCreateView(CreateView):
    model = Donasi
    form_class = DonasiForm
    success_url = reverse_lazy('donatur:donatur_list')