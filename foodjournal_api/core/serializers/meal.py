from rest_framework import serializers

from foodjournal_api.core.models.meal import Meal


class MealSerializer(serializers.ModelSerializer):
	"""
	Meal Model Serializer
	"""
	class Meta:
		model = Meal
		fields = (
			'id',
			'meal',
		)
