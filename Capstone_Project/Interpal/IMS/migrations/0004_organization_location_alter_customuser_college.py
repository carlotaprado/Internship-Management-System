# Generated by Django 5.0.2 on 2024-11-28 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMS', '0003_alter_customuser_college'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='college',
            field=models.CharField(blank=True, choices=[('College of Arts and Humanities', 'College of Arts and Humanities'), ('College of Business and Accountancy', 'College of Business and Accountancy'), ('College of Criminal Justice Education', 'College of Criminal Justice Education'), ('College of Engineering, Architecture, and Technology', 'College of Engineering, Architecture, and Technology'), ('College of Hospitality Management and Tourism', 'College of Hospitality Management and Tourism'), ('College of Nursing and Health Sciences', 'College of Nursing and Health Sciences'), ('College of Sciences', 'College of Sciences'), ('College of Teacher Education', 'College of Teacher Education')], max_length=255, null=True),
        ),
    ]