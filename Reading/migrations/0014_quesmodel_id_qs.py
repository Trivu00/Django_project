# Generated by Django 3.2.8 on 2021-11-17 06:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Reading', '0013_readingbook_reading_translate'),
    ]

    operations = [
        migrations.AddField(
            model_name='quesmodel',
            name='id_qs',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
