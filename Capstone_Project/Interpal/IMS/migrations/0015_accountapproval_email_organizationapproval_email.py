# Generated by Django 5.0.2 on 2024-12-05 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMS', '0014_organizationapproval'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountapproval',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='organizationapproval',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
