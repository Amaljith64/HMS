# Generated by Django 4.0.7 on 2022-08-25 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0016_alter_multiimg_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MultiImg',
            new_name='MultiImage',
        ),
    ]