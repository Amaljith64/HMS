# Generated by Django 4.0.3 on 2022-08-22 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0011_hotelbookings_delete_hotelbooking'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelbookings',
            name='payment_method',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
