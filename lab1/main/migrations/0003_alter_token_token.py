# Generated by Django 5.0.1 on 2024-03-14 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(max_length=255),
        ),
    ]