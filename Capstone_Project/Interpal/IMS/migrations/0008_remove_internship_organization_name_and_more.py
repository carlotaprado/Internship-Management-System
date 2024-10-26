# Generated by Django 5.1.1 on 2024-10-23 02:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMS', '0007_remove_customuser_organization_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='internship',
            name='organization_name',
        ),
        migrations.AddField(
            model_name='customuser',
            name='organization',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to='IMS.organization'),
        ),
        migrations.AddField(
            model_name='organization',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='organization',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='internship',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='internships', to='IMS.organization'),
        ),
        migrations.DeleteModel(
            name='Application',
        ),
    ]
