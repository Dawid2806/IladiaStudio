# Generated by Django 5.0.1 on 2024-06-23 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iladia', '0003_rename_client_id_nailsimages_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nailsimages',
            name='client',
        ),
    ]
