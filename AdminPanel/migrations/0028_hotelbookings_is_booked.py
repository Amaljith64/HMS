# Generated by Django 4.0.3 on 2022-09-06 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0027_category_offer_discount_room_offer_discount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelbookings',
            name='is_booked',
            field=models.BooleanField(default=False),
        ),
    ]