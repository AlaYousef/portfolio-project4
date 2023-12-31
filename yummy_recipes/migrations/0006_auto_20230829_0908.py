# Generated by Django 3.2.20 on 2023-08-29 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yummy_recipes', '0005_auto_20230829_0859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='cook_time',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='min_hour',
        ),
        migrations.AddField(
            model_name='recipe',
            name='cook_prepare_time',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=1),
        ),
    ]
