# Generated by Django 3.0.5 on 2020-04-09 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200404_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
