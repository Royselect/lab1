# Generated by Django 5.0.1 on 2024-05-05 13:10

import main.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_user_options_rename_is_admin_user_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='custompermission',
            managers=[
                ('objects', main.models.CustomUserManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='customrole',
            managers=[
                ('objects', main.models.CustomUserManager()),
            ],
        ),
    ]