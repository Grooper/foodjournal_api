from rest_framework import serializers

from foodjournal_api.core.models.food_group import FoodGroup


class FoodGroupSerializer(serializers.ModelSerializer):
	"""
	FoodGroup Model Serializer
	"""
	class Meta:
		model = FoodGroup
		fields = (
			'id',
			'food_group',
		)
