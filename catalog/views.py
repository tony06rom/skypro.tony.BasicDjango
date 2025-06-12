from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from catalog.forms import ProductForm
from catalog.models import Contact, Product
from django.contrib.auth.mixins import LoginRequiredMixin


class ContactCreateView(CreateView):
    model = Contact
    template_name = "catalog/contacts.html"
    fields = ["name", "phone", "message"]
    success_url = reverse_lazy("catalog:contacts")
    context_object_name = "contacts"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Данные получены! Спасибо за обращение.")
        return response


class ProductListView(ListView):
    model = Product
    template_name = "catalog/products_list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_add.html'
    success_url = reverse_lazy('catalog:products_list')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_update.html'

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_del.html'
    success_url = reverse_lazy('catalog:products_list')