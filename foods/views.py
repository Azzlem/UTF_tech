from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from foods.models import FoodCategory
from foods.serializers import FoodListSerializer


class FoodListView(APIView):
    def get(self, request):
        categories = FoodCategory.objects.filter(food__is_publish=True).distinct()
        serializer = FoodListSerializer(categories, many=True)
        return Response(serializer.data)
