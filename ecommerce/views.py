from decimal import Decimal
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView, GenericAPIView
# from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from openpyxl import Workbook
from django.http import HttpResponse
from django.db.models import F, Q
from .models import Product, Category, CartItem, CollectionItem
from accounts.models import User
from .serializers import ProductSerializer, CategorySerializer, ManageProductSerializer, ProductApiSerializer
from .filters import ProductFilter
from helpers.pagination import CustomPageNumberPagination
from helpers.functions import create_excel_table, bar, line, pie
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from helpers.styles import DEFAULT_STYLE_DIC
import os
import json

# Create your views here.
class ListFilterItems(ListAPIView):
    # Define serializer class
    serializer_class = ProductSerializer

    # Pagination class
    pagination_class = CustomPageNumberPagination

    filterset_class = ProductFilter

    # permission_classes = [AllowAny]

    # Retrieve all items
    queryset = Product.objects.all()

    # def get(self, request, *args, **kwargs):
    #     time.sleep(2)

    #     queryset = self.filter_queryset(self.get_queryset())
    #     page = self.paginate_queryset(queryset)

    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)

    #     serializer = self.get_serializer(queryset, many=True)

    #     return Response(serializer.data)

class ListItemsAPIView(ListAPIView):
    # Define serializer class
    serializer_class = ProductSerializer

    # Pagination class
    # pagination_class = CustomPageNumberPagination

    filterset_class = ProductFilter

    # Filters
    # filter_backends = [DjangoFilterBackend,
    #                 filters.SearchFilter, filters.OrderingFilter]

    # permission_classes = [AllowAny]

    # search_fields = ['name', 'price']
    # Retrieve all items
    # ordering_fields = ['price', 'stock']

    # Retrieve all items
    def get_queryset(self):
        return Product.objects.all()

class CreateItemAPIView(CreateAPIView):
    queryset = Product.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = ManageProductSerializer

class ItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    # Define serializer class
    serializer_class = ProductSerializer

    # permission_classes = [AllowAny]

    # Define look up field
    lookup_field = "id"

    def get_queryset(self):
        return Product.objects.filter(id=self.kwargs['id'])
    
    def perform_destroy(self, instance):
        if instance.image:
            instance.image.delete(save=False)
        instance.delete()

class AddItemToCart(GenericAPIView):

    def post(self, request, *args, **kwargs):
        user_pk = request.user.pk
        item_pk = self.kwargs.get('id')
        filtered_user_item = request.user.items.filter(product_id=item_pk)
        filtered_product = Product.objects.filter(id=item_pk)

        if filtered_product[0].stock == 0:
            raise ValidationError({
                'ok': False,
                'message': 'Sold out'
            })
        else:
            filtered_product.update(stock=F('stock') - 1)

        counter = filtered_user_item.count()
        if counter > 0:
            # update() devuelve el número de filas afectadas, no un objeto .save()
            filtered_user_item.update(quantity=F('quantity') + 1)
            quantity = filtered_user_item[0].quantity
        else:
            # create new cart item based on actually user & item's pk from request url
            cart_item = CartItem.objects.create(user_id=user_pk, product_id=item_pk)
            cart_item.save()
            quantity = 1
        
        stock = filtered_product[0].stock

        return Response({
            'ok': True,
            'stock_cart': quantity,
            'stock_gallery': stock
        })
    
    def delete(self, request, *args, **kwargs):
        item_pk = self.kwargs.get('id')
        filtered_item = request.user.items.filter(product_id=item_pk)

        if filtered_item.count() == 0:
            raise ValidationError({
                'ok': False,
                'message': 'Not found item'
            })

        filtered_item.update(quantity=F('quantity') - 1)
        product = Product.objects.filter(id=item_pk)
        product.update(stock=F('stock')+1)
        stock = product[0].stock
        
        if filtered_item[0].quantity == 0:
            filtered_item.delete()
            
            return Response({
                'ok': True,
                'message': 'Removed item'
            })
        else:
            quantity = filtered_item[0].quantity

        return Response({
            'ok': True,
            'stock_cart': quantity,
            'stock_gallery': stock 
        })

class BuyItem(GenericAPIView):

    def post(self, request, *args, **kwargs):
        # main variables
        user_pk = request.user.pk
        item_pk = self.kwargs.get('id')
        filtered_item = request.user.collection.filter(product_id=item_pk)
        cart_item = request.user.items.filter(product_id=item_pk)
        item = Product.objects.get(id=item_pk)
        price = item.price

        new_collection_item = False

        if cart_item.count() == 0:
            raise ValidationError({
                'ok': False,
                'message': 'Not found item'
            })

        counter = filtered_item.count()
        if counter > 0:
            # update() devuelve el número de filas afectadas, no un objeto .save()
            filtered_item.update(quantity=F('quantity') + 1)
            stock_collection = filtered_item[0].quantity
        else:
            # create new cart item based on actually user & item's pk from request url
            new_item = CollectionItem.objects.create(user_id=user_pk, product_id=item_pk)
            new_item.save()
            stock_collection = new_item.quantity
            new_collection_item = True
        
        user = User.objects.filter(id=user_pk)
        user.update(balance=F('balance')-price)
        balance = user[0].balance
        
        cart_item.update(quantity=F('quantity')-1)
        if cart_item[0].quantity == 0:
            cart_item.delete()
            return Response({
                'ok': True,
                'stock_collection': stock_collection,
                'new_collection_item': new_collection_item,
                'balance': balance
            })
        else:
            shopping_cart_state = cart_item[0].quantity

        return Response({
            'ok': True,
            'stock_collection': stock_collection,
            'new_collection_item': new_collection_item,
            'stock_cart': shopping_cart_state,
            'balance': balance
        })

    def delete(self, request, *args, **kwargs):
        user_pk = request.user.pk
        item_pk = self.kwargs.get('id')
        item = Product.objects.filter(id=item_pk)
        collection_item = request.user.collection.filter(product_id=item_pk)
        price = item[0].price

        if collection_item.count() == 0:
            raise ValidationError({
                'ok': False,
                'message': 'Not found item'
            })
        
        user = User.objects.filter(id=user_pk)
        user.update(balance=F('balance')+price)
        balance = user[0].balance

        item.update(stock=F('stock')+1)
        stock = item[0].stock
        collection_item.update(quantity=F('quantity')-1)

        if collection_item[0].quantity == 0:
            collection_item.delete()
            return Response({
                'ok': True,
                'message': f'Removed item',
                'stock_gallery': stock,
                'balance': balance
            })
        else:
            collection_items = collection_item[0].quantity

        return Response({
            'ok': True,
            'stock_collection': collection_items,
            'stock_gallery': stock,
            'balance': balance
        })

class CategoryAPIView(ListAPIView):
    # Define serializer class
    serializer_class = CategorySerializer
    # permission_classes = [AllowAny]
    # Pagination class
    queryset = Category.objects.all()

def EcommerceExcelReport(request):
    # Create new excel worksheet
    wb = Workbook()
    ws = wb.active
    ws.title = "Excel stadistics report"  # worksheet name

    items = Product.objects.all()

    most_expensive_items = items.order_by('-price')[:10]

    x_headers = [f"Item - {item.pk}" for item in most_expensive_items]
    graph_values = [int(item.price) for item in most_expensive_items]

    PROPERTIES = {
        'figsize': (10,4),
        'labels': x_headers,
        'graph_values': graph_values,
        'colors': ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:brown', 'tab:purple', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'],
        'y_title': 'Decreasing values',
        'x_title': 'Item id axis',
        'main_title': 'Most expensive gallery',
        'position': 'B2',
        'legend': True,
        'facecolor': '#15A9AB',
        'background': '#1290A6',
        'legend_title': 'Item list',
        'edgecolor': 'black',
        'bbox_to_anchor': (1.3, 0.8),
        'font_size': 9,
        'ha': 'center',
        'fontweight': 'bold',
        'border_linewidth': 3,
        'border_color': 'black',
        'margins_y': 0.2
        }

    bar(ws, PROPERTIES)

    PROPERTIES.update({'position': 'B23', 'marker': 'o', 'linestyle': '-', 'plot_color': 'black', 'linewidth': 0.5, 'font_size': 10, 'color': 'black', 'plot_text_color': 'yellow'})

    line(ws, PROPERTIES)

    PROPERTIES.pop('y_title')
    PROPERTIES.pop('x_title')

    PROPERTIES.update({'position': 'AH2',
                        'font': 'Courier New',
                        'weight': 'light',
                        'size': 11,
                        'shadow': True,
                        'bbox_to_anchor': (1.2,.8),
                        'autopct': '%1.1f%%'
                        })

    pie(ws, PROPERTIES)

    cheapest_items = items.order_by('price')[:10]
    x_headers = [f"Item - {item.pk}" for item in cheapest_items]
    cheapest_items = [int(item.price) for item in cheapest_items]

    PROPERTIES.update({'position': 'R2', 'labels': x_headers, 'graph_values': cheapest_items,
                    'main_title': 'Cheapest gallery', 'y_title': 'Increasing values', 'bbox_to_anchor': (1.3, 0.8)})

    bar(ws, PROPERTIES)

    PROPERTIES.update({'position': 'O23', 'font_size': 10})

    line(ws, PROPERTIES)

    PROPERTIES.pop('y_title')

    PROPERTIES.update({'position': 'AB24',
                    'bbox_to_anchor': (1.2,.8)})

    pie(ws, PROPERTIES)

    # Second worksheet
    tables_sheet = wb.create_sheet(title="Data")

    # Create table data
    main_data = {}

    for i in range(0,5):
        main_data['id'] = [current_item.pk for current_item in items[i*6:(i+1)*6]]
        main_data['Product'] = [current_item.name for current_item in items[i*6:(i+1)*6]]
        main_data['Price'] = [f'$ {current_item.price:,}' for current_item in items[i*6:(i+1)*6]]
        main_data['Categories'] = [', '.join(list(current_item.categories.values_list('name', flat=True))).replace('.','') for current_item in items[i*6:(i+1)*6]]
        create_excel_table(tables_sheet, main_data, DEFAULT_STYLE_DIC, (i*8+2, 2))
        main_data = {}

    # Prepare your response as a .xlsx file
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=reporte_estadisticas.xlsx'

    wb.save(response)

    return response

class ProductGeneric(viewsets.ModelViewSet):
    serializer_class = ProductApiSerializer
    # permission_classes = [AllowAny]
    queryset = Product.objects.all()

def list_items(request):
    AUTH_TOKEN = os.getenv('AUTH_TOKEN')
    queryset = Product.objects.all()
    sub_queryset = queryset[:8]
    categories = Category.objects.all()

    #* ---
    name__filter = request.GET.get("name")
    #
    categories__filter = request.GET.getlist("categories")
    #
    price__min = request.GET.get('price__min') or 199
    price__max = request.GET.get('price__max') or 2001
    stock__min = request.GET.get('stock__min') or 0
    stock__max = request.GET.get('stock__max') or 31
    #
    price__ordering = request.GET.get('price__ordering') or None
    stock__ordering = request.GET.get('stock__ordering') or None
    priority__param = request.GET.get('priority') or None

    has_data = any(value for value in request.GET.values())
    if has_data:
        filters = Q()

        if name__filter:
            filters &= Q(name__icontains=name__filter)
            
        if categories__filter:
            filters &= Q(categories__id__in=categories__filter)

        filters &= Q(price__gt=price__min)
        filters &= Q(price__lt=price__max)
        filters &= Q(stock__gt=stock__min)
        filters &= Q(stock__lt=stock__max)
        
        queryset = queryset.filter(filters).distinct()

        if price__ordering and stock__ordering:
            if priority__param == 'price':
                queryset = queryset.order_by(price__ordering, stock__ordering)
            elif priority__param == 'stock':
                queryset = queryset.order_by(stock__ordering, price__ordering)
        elif price__ordering or stock__ordering:
            final_param = price__ordering or stock__ordering
            queryset = queryset.order_by(final_param)

        sub_queryset = queryset[:8]

    sub_queryset = [model_to_dict(item) for item in sub_queryset]
    sub_queryset = [{**item,
    'image': item['image'].url,
    'categories': [category.name for category in item['categories']]
    } for item in sub_queryset]

    js__queryset = [model_to_dict(item) for item in queryset]
    js__queryset = [{**item,
    'image': item['image'].url,
    'categories': [category.name for category in item['categories']]
    } for item in js__queryset]

    template = 'ecommerce/list.html'
    context = {
        'queryset': json.dumps(js__queryset, cls=DjangoJSONEncoder),
        'sub_queryset': sub_queryset,
        'auth_token': AUTH_TOKEN,
        'categories': categories
    }

    return render(request, template, context)

def shopping_cart(request):
    AUTH_TOKEN = os.getenv('AUTH_TOKEN')

    user = request.user
    #items
    items = user.items.all()
    item_stocks = [item.quantity for item in items]
    items = [model_to_dict(item.product) for item in items]
    item_categories = [', '.join([sub_item.name.replace('.','') for sub_item in item['categories']]) for item in items]
    # collection 
    collection = user.collection.all()
    collection_stocks = [item.quantity for item in collection]
    collection = [model_to_dict(item.product) for item in collection]
    collection_categories = [', '.join([sub_item.name.replace('.','') for sub_item in item['categories']]) for item in collection]

    template = 'ecommerce/shopping_cart.html'
    context = {
        'user': user,
        'items': zip(items, item_stocks, item_categories),
        'collection': zip(collection, collection_stocks, collection_categories),
        'auth_token': AUTH_TOKEN
    }

    return render(request, template, context)
