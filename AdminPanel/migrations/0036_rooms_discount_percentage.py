# Generated by Django 4.0.3 on 2022-09-12 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0035_couponstatus_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='discount_percentage',
            field=models.IntegerField(null=True),
        ),
    ]