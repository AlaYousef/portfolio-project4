# Generated by Django 3.2.20 on 2023-07-30 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yummy_recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.IntegerField(choices=[(0, 'Dinner'), (1, 'Sweets'), (2, 'Coctailes')], default=0),
        ),
    ]
