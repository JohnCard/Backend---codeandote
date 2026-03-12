from django.urls import path, include
#! Este generador ya se considera antiguo
# from rest_framework.documentation import include_docs_urls
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework import routers
from .views import ListItemsAPIView, ItemRetrieveUpdateDestroyAPIView, CategoryAPIView, EcommerceExcelReport, CreateItemAPIView, ListFilterItems, ProductGeneric

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
    # List category instances
    path('categories', CategoryAPIView.as_view(), name='category_list'),
    # Generate excel report
    path('ecommerce-report', EcommerceExcelReport, name='report'),
    # api router
    path('item-api/', include(router.urls)),
    # product api documentation
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs')
]