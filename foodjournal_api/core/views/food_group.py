from rest_framework import viewsets

from foodjournal_api.core.models.food_group import FoodGroup
from foodjournal_api.core.serializers.food_group import FoodGroupSerializer


class FoodGroupViewSet(viewsets.ModelViewSet):
	"""
	Endpoint for `FoodGroup` Model
	"""
	queryset = FoodGroup.objects.all()
	serializer_class = FoodGroupSerializer
	filter_fields = ()
