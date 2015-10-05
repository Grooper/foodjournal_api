from rest_framework import serializers

from foodjournal_api.core.models.item import Item


class ItemSerializer(serializers.ModelSerializer):
	"""
	Item Model Serializer
	"""
	total_calories = serializers.SerializerMethodField()
	food_name = serializers.SerializerMethodField()
	meal_name = serializers.SerializerMethodField()
	food_group = serializers.SerializerMethodField()

	def get_total_calories(self, obj):
		"""
		Get the total calories of this entry (num_servings * cals_per_serving)
		"""
		return obj.num_servings * obj.food.cals_per_serving

	def get_food_name(self, obj):
		"""
		Get the name of this food
		"""
		return obj.food.name

	def get_meal_name(self, obj):
		"""
		Get the name of this meal
		"""
		return obj.meal.meal

	def get_food_group(self, obj):
		"""
		Get the food group of this food
		"""
		return obj.food.food_group.food_group

	class Meta:
		model = Item
		fields = (
			'id',
			'num_servings',
			'meal_date',
			'food',
			'meal',
			'total_calories',
			'food_name',
			'meal_name',
			'food_group',
		)
