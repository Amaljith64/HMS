# Generated by Django 4.0.3 on 2022-08-16 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccountSection', '0014_alter_userotp_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userotp',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x000001E18F8A88B0>', max_length=200),
        ),
    ]
