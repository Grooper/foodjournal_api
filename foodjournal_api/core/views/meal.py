from rest_framework import viewsets

from foodjournal_api.core.models.meal import Meal
from foodjournal_api.core.serializers.meal import MealSerializer


class MealViewSet(viewsets.ModelViewSet):
	"""
	Endpoint for `Meal` Model
	"""
	queryset = Meal.objects.all()
	serializer_class = MealSerializer
	filter_fields = ()
