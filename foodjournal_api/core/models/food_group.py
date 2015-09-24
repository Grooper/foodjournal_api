from django.db import models


class FoodGroupManager(models.Manager):
	"""
	Food Group Model Manager
	"""
	pass

class Meal(models.Model):
	"""
	Food Group Model
	"""
	food_group = models.CharField(max_length=20, unique=True)

	objects = FoodGroupManager()
