# Generated by Django 4.0.3 on 2022-09-04 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payments', '0002_paymentclass_booked_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentclass',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='paymentclass',
            name='status',
            field=models.CharField(default='pending', max_length=100),
        ),
    ]
