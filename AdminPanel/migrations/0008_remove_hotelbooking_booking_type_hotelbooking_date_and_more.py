# Generated by Django 4.0.3 on 2022-08-20 09:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0007_rooms_room_count_hotelbooking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelbooking',
            name='booking_type',
        ),
        migrations.AddField(
            model_name='hotelbooking',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotelbooking',
            name='status',
            field=models.CharField(default='pending', max_length=100, null=True),
        ),
    ]
