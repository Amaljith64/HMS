# Generated by Django 4.0.3 on 2022-08-20 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccountSection', '0028_alter_userotp_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userotp',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x0000028860EC88B0>', max_length=200),
        ),
    ]
