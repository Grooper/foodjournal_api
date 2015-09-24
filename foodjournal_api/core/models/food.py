from django.db import models


class FoodManager(models.Manager):
	"""
	Food Model Manager
	"""
	pass

class Food(models.Model):
	"""
	Food Model
	"""
	name = models.CharField(max_length=30, unique=True)
	cals_per_serving = models.IntegerField()

	food_group = models.ForeignKey('core.FoodGroup', related+name='foods')

	objects = FoodManager()
