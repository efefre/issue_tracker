# Generated by Django 3.0.3 on 2020-02-17 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0015_auto_20200216_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('in progress', 'In progress'), ('success', 'Success'), ('cancel', 'Cancel')], default='in progress', max_length=20, verbose_name='Project status'),
        ),
    ]