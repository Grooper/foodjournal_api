# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30)),
                ('cals_per_serving', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FoodGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('food_group', models.CharField(unique=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num_servings', models.FloatField()),
                ('meal_date', models.DateTimeField(auto_now_add=True)),
                ('food', models.ForeignKey(related_name='items', to='core.Food')),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meal', models.CharField(unique=True, max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='meal',
            field=models.ForeignKey(related_name='items', to='core.Meal'),
        ),
        migrations.AddField(
            model_name='food',
            name='food_group',
            field=models.ForeignKey(related_name='foods', to='core.FoodGroup'),
        ),
    ]
