# Generated by Django 5.0.1 on 2024-06-23 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iladia', '0006_alter_nailsimages_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tattooimages',
            name='client',
        ),
    ]
