# Generated by Django 4.2.7 on 2023-12-07 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_alter_surverysubmit_season'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surverysubmit',
            name='areas',
            field=models.BooleanField(verbose_name=('putting', 'driving', 'chipping', 'approuching', 'idk')),
        ),
    ]
