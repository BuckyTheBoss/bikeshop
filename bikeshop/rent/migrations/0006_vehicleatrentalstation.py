# Generated by Django 2.1.7 on 2019-04-05 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0005_auto_20190402_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleAtRentalStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_date', models.DateTimeField()),
                ('departure_date', models.DateTimeField(null=True)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.Vehicle')),
            ],
        ),
    ]