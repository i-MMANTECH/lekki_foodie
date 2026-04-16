# URLs map request to views in the restaurants app


from django.urls import path
from .views import RestaurantListCreate, RestaurantDetail

urlpatterns = [
    path('restaurants/', RestaurantListCreate.as_view(), name='restaurant-list-create'),
    path('restaurants/<int:pk>/', RestaurantDetail.as_view(), name='restaurant-detail'),
]