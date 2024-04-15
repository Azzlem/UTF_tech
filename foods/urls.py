from django.urls import path

from foods.apps import FoodsConfig
from foods.views import FoodListView

app_name = FoodsConfig.name

urlpatterns = [
    path('api/v1/foods/', FoodListView.as_view(), name='food-list'),
]
