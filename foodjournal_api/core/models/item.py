from django.db import models


class ItemManager(models.Manager):
	"""
	Item Model Manager
	"""
	pass

class Item(models.Model):
	"""
	Item Model
	"""
	num_servings = models.FloatField()
	meal_date = models.DateTimeField(auto_now_add=True)

	food = models.ForeignKey('core.Food', related_name='items')
	meal = models.ForeignKey('core.Meal', related_name='items')

	objects = ItemManager()
