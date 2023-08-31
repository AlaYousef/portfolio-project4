# Generated by Django 3.2.20 on 2023-08-29 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yummy_recipes', '0012_recipe_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='min_hour',
            field=models.IntegerField(choices=[(0, 'Min'), (1, 'Hour')], default=1),
        ),
    ]