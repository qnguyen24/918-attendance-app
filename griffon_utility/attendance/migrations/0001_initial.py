# Generated by Django 3.0.2 on 2020-01-08 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('nickname', models.CharField(max_length=100)),
                ('useNickname', models.BooleanField(default=False)),
                ('attendancePercentage', models.FloatField(blank=True)),
                ('cadets', models.ManyToManyField(related_name='_flight_cadets_+', to='attendance.Cadet')),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('cadetsPresent', models.ManyToManyField(to='attendance.Cadet')),
            ],
        ),
        migrations.AddField(
            model_name='cadet',
            name='daysPresent',
            field=models.ManyToManyField(blank=True, to='attendance.Day'),
        ),
        migrations.AddField(
            model_name='cadet',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='attendance.Flight'),
        ),
    ]
