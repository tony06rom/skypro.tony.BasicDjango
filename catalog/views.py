from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from catalog.forms import ProductForm, StyleFormMixin, ProductModeratorForm
from catalog.models import Contact, Product
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


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

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.has_perm('catalog.can_view_unpublished'):
            queryset = queryset.filter(is_published=True)
        return queryset.order_by('name')


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_detail.html"


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_add.html'
    success_url = reverse_lazy('catalog:products_list')
    permission_required = 'catalog.can_add_product'

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_update.html'
    permission_required = 'catalog.can_change_product'

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_change_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_del.html'
    success_url = reverse_lazy('catalog:products_list')
    permission_required = 'catalog.can_delete_product'


class ProductPublishView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'catalog/product_publish.html'
    permission_required = 'catalog.can_unpublish_product'
    fields = []

    def form_valid(self, form):
        product = form.save(commit=False)
        product.is_published = True
        product.save()
        messages.success(self.request, f'Товар "{product.name}" опубликован')
        return redirect('catalog:product_detail', pk=product.pk)


class ProductUnpublishView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'catalog/product_unpublish.html'
    permission_required = 'catalog.can_unpublish_product'
    fields = []

    def form_valid(self, form):
        product = form.save(commit=False)
        product.is_published = False
        product.save()
        messages.success(self.request, f'Товар "{product.name}" снят с публикации')
        return redirect('catalog:product_detail', pk=product.pk)
