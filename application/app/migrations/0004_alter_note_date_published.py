# Generated by Django 4.0.4 on 2022-04-21 08:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_note_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date_published',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации'),
        ),
    ]
