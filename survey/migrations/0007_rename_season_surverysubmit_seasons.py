# Generated by Django 4.2.7 on 2023-12-09 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_alter_surverysubmit_areas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surverysubmit',
            old_name='season',
            new_name='seasons',
        ),
    ]