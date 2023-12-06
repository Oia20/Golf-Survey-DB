# Generated by Django 4.2.7 on 2023-12-06 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_alter_surverysubmit_strokes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surverysubmit',
            name='years',
            field=models.CharField(choices=[('less than one.', 'less than one.'), ('one', 'one'), ('three', 'three'), ('four', 'four'), ('five', 'five'), ('six or more.', 'six or more.')], default='one', max_length=30),
        ),
    ]