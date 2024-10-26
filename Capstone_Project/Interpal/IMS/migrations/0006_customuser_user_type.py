# Generated by Django 5.1.1 on 2024-10-23 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMS', '0005_alter_organization_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('student', 'Student'), ('organization', 'Organization'), ('admin', 'Admin')], default='student', max_length=20),
        ),
    ]
