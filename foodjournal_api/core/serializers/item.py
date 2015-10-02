from rest_framework import serializers

from foodjournal_api.core.models.item import Item


class ItemSerializer(serializers.ModelSerializer):
	"""
	Item Model Serializer
	"""
	class Meta:
		model = Item
		fields = (
			'id',
			'num_servings',
			'meal_date',
			'food',
			'meal',
		)
