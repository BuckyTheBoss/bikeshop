# Generated by Django 2.1.7 on 2019-04-05 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0006_vehicleatrentalstation'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicleatrentalstation',
            name='rental_station',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='rent.Rental_Station'),
            preserve_default=False,
        ),
    ]
