from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, home, products_list, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path("contacts_2/", contacts,name="contacts"),
    path("products_list/", products_list,name="products_list"),
    path("product/<int:pk>/", product_detail,name="product_detail")
]
