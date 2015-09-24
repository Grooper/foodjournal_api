from django.db import models


class MealManager(models.Manager):
	"""
	Meal Model Manager
	"""
	pass

class Meal(models.Model):
	"""
	Meal Model
	"""
	meal = models.CharField(max_length=20, unique=True)

	objects = MealManager()
