from config.settings import CACHE_ENABLED
from django.core.cache import cache
from catalog.models import Product, Category


def get_products_from_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


def get_all_categories():
    cache_key = 'all_categories'
    categories = cache.get(cache_key)
    if not categories:
        categories = Category.objects.all()
        cache.set(cache_key, categories, timeout=3600)
    return categories


def get_products_by_category(category_id):
    if not category_id:
        return Product.objects.none()

    cache_key = f'products_by_category_{category_id}'
    products = cache.get(cache_key)
    if not products:
        products = Product.objects.filter(
            category_id=category_id,
            is_published=True
        ).select_related('category')
        cache.set(cache_key, products, timeout=3600)
    return products
