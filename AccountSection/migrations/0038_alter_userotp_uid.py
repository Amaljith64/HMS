# Generated by Django 4.0.3 on 2022-08-20 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccountSection', '0037_alter_userotp_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userotp',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x0000025F8FFF88B0>', max_length=200),
        ),
    ]
