# Generated by Django 4.0.3 on 2022-08-31 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0020_alter_multiimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]