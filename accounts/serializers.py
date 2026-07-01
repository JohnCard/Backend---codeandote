from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import User


def _image_url(obj):
    if not obj.image or not obj.image.name:
        return None
    try:
        return obj.image.url
    except (OSError, ValueError):
        return None


class UserSerializer(ModelSerializer):
    image = SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'balance', 'image']

    def get_image(self, obj):
        return _image_url(obj)