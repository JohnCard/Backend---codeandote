from django.urls import path, include
#! Este generador ya se considera antiguo
# from rest_framework.documentation import include_docs_urls
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework import routers
from .views import ListItemsAPIView, ItemRetrieveUpdateDestroyAPIView, CategoryAPIView, EcommerceExcelReport, CreateItemAPIView, ListFilterItems, ProductGeneric, AddItemToCart, BuyItem, list_items, shopping_cart

# api versioning
router = routers.DefaultRouter()
router.register(r'items', ProductGeneric, 'items')

urlpatterns = [
    #* List item instances
    path('gallery', ListItemsAPIView.as_view(), name='gallery'),
    #* Gallery by filters
    path('gallery-filters', ListFilterItems.as_view(), name='gallery_filters'),
    #* Retrieve, update & delete item instances
    path('gallery/<int:id>', ItemRetrieveUpdateDestroyAPIView.as_view(), name='gallery_retrieve'),
    #* Create item instances
    path('gallery-create', CreateItemAPIView.as_view(), name='gallery_create'),
    #* List category instances
    path('categories', CategoryAPIView.as_view(), name='category_list'),
    #* api router - second CRUD for product model
    path('item-api/', include(router.urls)),
    #* Generate excel report
    path('gallery-report', EcommerceExcelReport, name='report'),
    # product api documentation
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    #* Add item to shopping cart
    path('add-item/<int:id>', AddItemToCart.as_view(), name='add-item'),
    #* Buy item
    path('buy-item/<int:id>', BuyItem.as_view(), name='buy-item'),
    #todo HTML template views
    # list items
    path('list-items', list_items, name='list_items'),
    # shopping cart
    path('shopping-cart', shopping_cart, name='shopping_cart'),
]