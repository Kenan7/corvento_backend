# Generated by Django 3.0.5 on 2020-04-13 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_event_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='data',
            new_name='date',
        ),
    ]
