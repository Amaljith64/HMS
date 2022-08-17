# Generated by Django 4.0.3 on 2022-08-13 11:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AccountSection', '0007_rename_username_userotp_name_alter_userotp_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userotp',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userotp',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x00000276863488B0>', max_length=200),
        ),
    ]