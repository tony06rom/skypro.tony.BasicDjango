from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from catalog.models import Product
from django.views.generic import ListView, TemplateView, DetailView, CreateView


def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "contacts_2.html")


def contacts_post(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        email = request.POST.get("email")
        return HttpResponse(f"Введенные данные: {name}, {email}, {message}")
    return render(request, "catalog/contacts_2.html")


class ProductListView(ListView):
    model = Product
    # template_name = 'catalog/products_list.html'
    # context_object_name = 'products_list'
    # paginate_by = 6


# def products_list(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, 'products_list_fbv.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context)
