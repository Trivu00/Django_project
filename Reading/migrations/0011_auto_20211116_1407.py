# Generated by Django 3.2.8 on 2021-11-16 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reading', '0010_alter_readingbook_question_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readingbook',
            name='question_model',
        ),
        migrations.AddField(
            model_name='quesmodel',
            name='reading_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Reading.readingbook'),
        ),
    ]
