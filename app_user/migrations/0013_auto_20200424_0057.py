# Generated by Django 3.0.5 on 2020-04-23 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0012_appuser_firebase_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='uuid',
        ),
        migrations.AddField(
            model_name='appuser',
            name='id',
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]