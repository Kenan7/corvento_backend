# Generated by Django 3.0.5 on 2020-04-23 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0011_auto_20200424_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='firebase_id',
            field=models.CharField(default='3274862482', max_length=120),
            preserve_default=False,
        ),
    ]
