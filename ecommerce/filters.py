import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')  # Contiene
    price = django_filters.RangeFilter(field_name='price')
    stock = django_filters.RangeFilter(field_name='stock')
    categories__in = django_filters.BaseInFilter(field_name='categories', lookup_expr='in')
    ordering = django_filters.OrderingFilter(
        fields=(
            ("price", "price"),
            ("stock", "stock"),
        )
    )

    class Meta:
        model = Product
        fields = ['name', 'price', 'categories__in', 'stock']
