from rest_framework import viewsets

from foodjournal_api.core.models.food import Food
from foodjournal_api.core.serializers.food import FoodSerializer


class FoodViewSet(viewsets.ModelViewSet):
	"""
	Endpoint for `Food` Model
	"""
	queryset = Food.objects.all()
	serializer_class = FoodSerializer
	filter_fields = ('food_group',)
