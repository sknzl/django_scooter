# Generated by Django 2.2.4 on 2019-08-18 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scooter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scooter_id', models.CharField(max_length=255, unique=True)),
                ('last_lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('last_lng', models.DecimalField(decimal_places=6, max_digits=9)),
                ('last_activity_at', models.DateTimeField()),
                ('distance_travelled', models.FloatField(default=0)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScooterActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lng', models.DecimalField(decimal_places=6, max_digits=9)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('scooter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scooter.Scooter')),
            ],
        ),
    ]
