# Generated by Django 4.0.3 on 2022-08-20 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccountSection', '0024_alter_userotp_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userotp',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x00000200FE5A88B0>', max_length=200),
        ),
    ]
