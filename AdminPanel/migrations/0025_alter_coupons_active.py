# Generated by Django 4.0.3 on 2022-09-05 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0024_coupons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupons',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
