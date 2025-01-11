# Generated by Django 5.0.2 on 2024-12-04 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMS', '0011_alter_application_application_letter_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='location',
        ),
        migrations.AddField(
            model_name='organization',
            name='barangay',
            field=models.CharField(blank=True, choices=[('Irawan', 'Irawan'), ('San Rafael', 'San Rafael'), ('San Manuel', 'San Manuel'), ('San Pedro', 'San Pedro'), ('Rizal', 'Rizal'), ('Manalo', 'Manalo'), ('San Jose', 'San Jose'), ('Sta. Lourdes', 'Sta. Lourdes'), ('Sta. Monica', 'Sta. Monica'), ('Tagburos', 'Tagburos'), ('Balsahan', 'Balsahan'), ('Bagumbayan', 'Bagumbayan'), ('Bungtol', 'Bungtol'), ('Longlong', 'Longlong'), ('Sicsican', 'Sicsican'), ('Balsahan', 'Balsahan'), ('Tiniguiban', 'Tiniguiban'), ('Baywalk', 'Baywalk')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='city',
            field=models.CharField(default='Puerto Princesa', max_length=100),
        ),
        migrations.AddField(
            model_name='organization',
            name='province',
            field=models.CharField(default='Palawan', max_length=100),
        ),
        migrations.AddField(
            model_name='organization',
            name='zip_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
