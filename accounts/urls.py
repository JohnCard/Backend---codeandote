from django.urls import path
from .views import UserAPIView, UserReturn


urlpatterns = [
    # Retrieve user by it's primary key
    path('user/<int:id>', UserAPIView.as_view(), name='user'),
    path('user', UserReturn.as_view(), name='user-return')
]