# Generated by Django 3.0.2 on 2020-01-08 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_remove_day_cadetspresent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadet',
            name='flight',
        ),
    ]
