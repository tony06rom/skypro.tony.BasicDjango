from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ContactCreateView, ProductDetailView, ProductListView, ProductDeleteView, ProductUpdateView, \
    ProductCreateView, ProductUnpublishView, ProductPublishView

app_name = CatalogConfig.name


urlpatterns = [
    path("contacts/", ContactCreateView.as_view(), name="contacts"),
    path("products_list/", ProductListView.as_view(), name="products_list"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product_update/<int:pk>", ProductUpdateView.as_view(), name="product_update"),
    path("product_add/", ProductCreateView.as_view(), name="product_add"),
    path("product_del/<int:pk>", ProductDeleteView.as_view(), name="product_del"),
    path('product/<int:pk>/publish/', ProductPublishView.as_view(), name='product_publish'),
    path('product/<int:pk>/unpublish/', ProductUnpublishView.as_view(), name='product_unpublish'),
]
