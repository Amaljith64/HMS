# Generated by Django 4.0.3 on 2022-08-14 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccountSection', '0008_alter_userotp_name_alter_userotp_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userotp',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x0000025DEE369940>', max_length=200),
        ),
    ]
