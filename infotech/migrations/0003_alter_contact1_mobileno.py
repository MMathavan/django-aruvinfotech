# Generated by Django 5.0.6 on 2024-05-29 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infotech', '0002_remove_contact1_subject_contact1_mobileno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact1',
            name='mobileno',
            field=models.CharField(max_length=15),
        ),
    ]