from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, home, ProductListView, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path("contacts_2/", contacts,name="contacts"),
    path("products_list/", ProductListView.as_view(),name="products_list"),
    path("product/<int:pk>/", product_detail,name="product_detail")
]
