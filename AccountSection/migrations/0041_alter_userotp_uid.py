# Generated by Django 4.0.3 on 2022-08-20 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccountSection', '0040_alter_userotp_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userotp',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x0000015D11EB8940>', max_length=200),
        ),
    ]
