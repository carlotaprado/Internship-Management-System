# Generated by Django 5.0.2 on 2024-11-29 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMS', '0006_remove_internship_preferred_college_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='preferred_college',
            field=models.CharField(choices=[('College of Arts and Humanities', 'College of Arts and Humanities'), ('College of Business and Accountancy', 'College of Business and Accountancy'), ('College of Criminal Justice Education', 'College of Criminal Justice Education'), ('College of Engineering, Architecture, and Technology', 'College of Engineering, Architecture, and Technology'), ('College of Hospitality Management and Tourism', 'College of Hospitality Management and Tourism'), ('College of Nursing and Health Sciences', 'College of Nursing and Health Sciences'), ('College of Sciences', 'College of Sciences'), ('College of Teacher Education', 'College of Teacher Education')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internship',
            name='preferred_course',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
