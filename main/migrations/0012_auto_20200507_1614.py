# Generated by Django 3.0.5 on 2020-05-07 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_event_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='published',
            field=models.BooleanField(default=False, help_text='\n        Bu özellik varsayılan olarak\n        devre dışı olarak geliyor,\n        aktifleştirildiğinde,\n        etkinlik herkese görünür olur\n        ve bu bilgilerle kullanıcılara\n        bildirim gider\n        ', verbose_name='\n        Etkinliği paylaş ve BİLDİRİM gönder'),
        ),
    ]
