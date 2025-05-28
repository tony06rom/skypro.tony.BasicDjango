from http.client import responses
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Contact
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages


class ContactCreateView(CreateView):
    model = Contact
    template_name = 'catalog/contacts.html'
    fields = ['name', 'phone', 'message']
    success_url = reverse_lazy('catalog:contacts')
    context_object_name = 'contacts'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Данные получены! Спасибо за обращение.')
        return response


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/products_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
