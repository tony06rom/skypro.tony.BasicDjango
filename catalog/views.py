from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.mixins import OwnerOrModeratorMixin, OwnerRequiredMixin
from catalog.models import Contact, Product, Category
from catalog.services import get_products_from_cache, get_products_by_category, get_all_categories


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
        queryset = get_products_from_cache()
        if not self.request.user.has_perm("catalog.can_view_unpublished"):
            queryset = queryset.filter(is_published=True)
        return queryset.order_by("name")


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_detail.html"


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_add.html"
    success_url = reverse_lazy("catalog:products_list")
    login_url = reverse_lazy("users:user_login")
    permission_required = "catalog.can_add_product"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        form.instance.owner = self.request.user
        if self.request.user.has_perm("catalog.can_unpublish_product"):
            form.instance.is_published = form.cleaned_data.get("is_published", False)
        else:
            form.instance.is_published = False
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView, OwnerRequiredMixin):
    model = Product
    template_name = "catalog/product_update.html"
    login_url = reverse_lazy("users:user_login")

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})

    def get_form_class(self):
        if self.request.user.has_perm("catalog.can_change_product"):
            return ProductModeratorForm
        return ProductForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.get_form_class() == ProductForm:
            kwargs["user"] = self.request.user
        return kwargs

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        user = request.user
        if not (user == obj.owner or user.has_perm("catalog.can_change_product")):
            raise PermissionDenied("У вас нет прав для редактирования этого товара")
        return super().dispatch(request, *args, **kwargs)


class ProductDeleteView(LoginRequiredMixin, DeleteView, OwnerOrModeratorMixin):
    model = Product
    template_name = "catalog/product_del.html"
    success_url = reverse_lazy("catalog:products_list")
    permission_required = "catalog.can_delete_product"
    login_url = reverse_lazy("users:user_login")

    def test_func(self):
        obj = self.get_object()
        user = self.request.user
        return user == obj.owner or user.has_perm("catalog.can_delete_product")


class ProductPublishView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = "catalog/product_publish.html"
    permission_required = "catalog.can_unpublish_product"
    fields = []

    def form_valid(self, form):
        product = form.save(commit=False)
        product.is_published = True
        product.save()
        messages.success(self.request, f'Товар "{product.name}" опубликован')
        return redirect("catalog:product_detail", pk=product.pk)


class ProductUnpublishView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = "catalog/product_unpublish.html"
    permission_required = "catalog.can_unpublish_product"
    fields = []

    def form_valid(self, form):
        product = form.save(commit=False)
        product.is_published = False
        product.save()
        messages.success(self.request, f'Товар "{product.name}" снят с публикации')
        return redirect("catalog:product_detail", pk=product.pk)


class ProductsByCategoryView(ListView):
    template_name = 'catalog/products_by_category.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_id = self.request.GET.get('category')
        return get_products_by_category(category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = get_all_categories()
        selected_id = self.request.GET.get('category')
        if selected_id:
            context['selected_category'] = Category.objects.filter(
                id=selected_id
            ).first()
        return context
