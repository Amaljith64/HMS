# Generated by Django 4.0.7 on 2022-08-29 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccountSection', '0073_alter_userotp_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userotp',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x0000019D93F449D0>', max_length=200),
        ),
    ]