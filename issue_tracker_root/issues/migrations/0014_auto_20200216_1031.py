# Generated by Django 3.0.2 on 2020-02-16 10:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0013_auto_20200211_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^[A-Z]*$', 'Only capital letters are allowed.')]),
        ),
    ]