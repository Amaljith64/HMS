# Generated by Django 4.0.3 on 2022-09-07 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0028_hotelbookings_is_booked'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelbookings',
            name='status',
            field=models.CharField(default='Pending', max_length=50),
        ),
    ]
