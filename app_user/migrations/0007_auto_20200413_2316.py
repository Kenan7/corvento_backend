# Generated by Django 3.0.5 on 2020-04-13 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0006_auto_20200413_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='notifications',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_user.UserNotifications'),
        ),
    ]
