from rest_framework import serializers

from foodjournal_api.core.models.item import Item


class ItemSerializer(serializers.ModelSerializer):
	"""
	Item Model Serializer
	"""
	total_calories = serializers.SerializerMethodField()

	def get_total_calories(self, obj):
		"""
		Get the total calories of this entry (num_servings * cals_per_serving)
		"""
		return obj.num_servings * obj.food.cals_per_serving

	class Meta:
		model = Item
		fields = (
			'id',
			'num_servings',
			'meal_date',
			'food',
			'meal',
			'total_calories',
		)
