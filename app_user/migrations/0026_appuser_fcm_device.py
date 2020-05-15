# Generated by Django 3.0.5 on 2020-05-09 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fcm_django', '0005_auto_20170808_1145'),
        ('app_user', '0025_contactform_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='fcm_device',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fcm_django.FCMDevice'),
        ),
    ]