from django.urls import path, include
from rest_framework import routers
from .views import ListItemsAPIView, ItemRetrieveUpdateDestroyAPIView, CategoryAPIView, EcommerceExcelReport, CreateItemAPIView, ListFilterItems, ProductGeneric
from ecommerce import views

# api versioning
router = routers.DefaultRouter()
router.register(r'items', ProductGeneric, 'items')

urlpatterns = [
    # List item instances
    path('gallery', ListItemsAPIView.as_view(), name='gallery'),
    # Gallery by filters
    path('gallery-filters', ListFilterItems.as_view(), name='gallery_filters'),
    # Retrieve, update & delete item instances
    path('gallery/<int:id>', ItemRetrieveUpdateDestroyAPIView.as_view(), name='gallery_retrieve'),
    # Create item instances
    path('gallery-create', CreateItemAPIView.as_view(), name='gallery_create'),
    # Create & list category instances
    path('categories', CategoryAPIView.as_view(), name='category_list'),
    # Generate excel report
    path('ecommerce-report', EcommerceExcelReport, name='report'),
    # api router
    path('item-api/', include(router.urls)),
]