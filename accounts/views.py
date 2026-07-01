from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, GenericAPIView
from django.forms.models import model_to_dict
from .serializers import UserSerializer
from .models import User
from datetime import datetime
import time
# Create your views here.

class UserAPIView(RetrieveAPIView):
    # serializer_class
    serializer_class = UserSerializer

    lookup_field = 'id'

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['id'])

class UserReturn(GenericAPIView):

    def get(self, request, *args, **kwargs):
        id = request.user.id
        username = request.user.username
        name = request.user.first_name
        last_name = request.user.last_name
        email = request.user.email
        is_staff = request.user.is_staff
        is_active = request.user.is_active
        balance = request.user.balance
        description = request.user.description
        image = request.user.image.url

        created_at = request.user.created_at
        # Si ya es datetime, formatea directo; si viniera string ISO, parsea primero.
        if isinstance(created_at, str):
            created_at = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        created_at = created_at.strftime("%d/%m/%Y")

        user = User.objects.get(id=id)
        items = user.items.all()
        item_quantity_list = [item.quantity for item in items]
        items = [model_to_dict(item.product) for item in items]

        collection = user.collection.all()
        collection_quantity_list = [item.quantity for item in collection]
        collection = [model_to_dict(item.product, exclude=['stock']) for item in collection]

        counter = 0
        for product in collection:
            product['quantity'] = collection_quantity_list[counter]
            counter += 1
            product['image'] = product['image'].url
            product['categories'] = [category.name for category in product['categories']]

        counter = 0
        for product in items:
            product['quantity'] = item_quantity_list[counter]
            counter += 1
            product['image'] = product['image'].url
            product['categories'] = [category.name for category in product['categories']]

        time.sleep(3)

        return Response({
            'ok': True,
            'id': id,
            'username': username,
            'name': name,
            'last_name': last_name,
            'email': email,
            'is_staff': is_staff,
            'is_active': is_active,
            'balance': balance,
            'description': description,
            'image': image,
            'created_at': created_at,
            'items': items,
            'collection': collection
        })