# Generated by Django 4.0.3 on 2022-08-16 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccountSection', '0015_alter_userotp_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userotp',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x00000178367888B0>', max_length=200),
        ),
    ]
