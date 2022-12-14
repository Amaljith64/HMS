# Generated by Django 4.0.3 on 2022-09-06 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0026_category_offer_is_active_room_offer_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category_offer',
            name='discount',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room_offer',
            name='discount',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory_offer',
            name='discount',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
    ]
