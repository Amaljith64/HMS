# Generated by Django 4.0.3 on 2022-09-10 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0031_rename_couponuser_couponstatus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='couponstatus',
            old_name='coupons',
            new_name='couponsid',
        ),
    ]