# Generated by Django 5.0.2 on 2024-11-29 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMS', '0004_organization_location_alter_customuser_college'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='preferred_college',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internship',
            name='preferred_course',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]