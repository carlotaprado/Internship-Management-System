# Generated by Django 5.0.2 on 2024-12-04 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMS', '0012_remove_organization_location_organization_barangay_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='barangay',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='city',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='province',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='organization',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
    ]