# Generated by Django 3.0.5 on 2020-04-04 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='event',
            old_name='title',
            new_name='name',
        ),
    ]
