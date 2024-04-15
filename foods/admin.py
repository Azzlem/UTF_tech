from django.contrib import admin

from foods.models import Food, FoodCategory

admin.site.register(FoodCategory)
admin.site.register(Food)
