# Generated by Django 3.0.5 on 2020-05-09 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20200509_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, unique=True),
        ),
    ]
