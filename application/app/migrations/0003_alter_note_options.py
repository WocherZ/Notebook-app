# Generated by Django 4.0.4 on 2022-04-20 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_note_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'verbose_name': 'Заметка', 'verbose_name_plural': 'Список заметок'},
        ),
    ]
