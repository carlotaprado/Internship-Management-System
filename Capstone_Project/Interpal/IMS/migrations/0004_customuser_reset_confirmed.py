# Generated by Django 5.1.1 on 2024-09-28 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMS', '0003_customuser_reset_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='reset_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
