# Generated by Django 4.0.3 on 2022-08-23 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0012_hotelbookings_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelbookings',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='hotelbookings',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]