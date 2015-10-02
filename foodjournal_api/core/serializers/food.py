from rest_framework import serializers

from foodjournal_api.core.models.food import Food


class FoodSerializer(serializers.ModelSerializer):
	"""
	Food Model Serializer
	"""
	food_group_name = serializers.SerializerMethodField()

	def get_food_group_name(self, obj):
		"""
		Get the name of the food group (starch, fat, protein, fruit, vegetable)
		"""
		return obj.food_group.food_group

	class Meta:
		model = Food
		fields = (
			'id',
			'name',
			'cals_per_serving',
			'food_group',
			'food_group_name',
		)
