# Generated by Django 2.2.9 on 2020-01-20 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0003_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='slug',
            field=models.SlugField(default='test', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]