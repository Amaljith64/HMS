# Generated by Django 4.0.3 on 2022-08-14 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccountSection', '0011_alter_userotp_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userotp',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x000002287B568940>', max_length=200),
        ),
    ]
