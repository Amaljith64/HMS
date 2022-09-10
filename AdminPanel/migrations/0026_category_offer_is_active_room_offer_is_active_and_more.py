# Generated by Django 4.0.3 on 2022-09-06 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0025_alter_coupons_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='category_offer',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='room_offer',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='subcategory_offer',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
