# Generated by Django 4.2.7 on 2023-12-06 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='surverySubmit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('strokes', models.IntegerField(max_length=300)),
                ('years', models.CharField(choices=[('less than one.', 'less than one.'), ('one', 'two'), ('three', 'three'), ('four', 'four'), ('five', 'five'), ('six or more.', 'six or more.')], default='one', max_length=30)),
                ('season', models.CharField(choices=[('summer', 'SUMMER'), ('spring', 'SPRING'), ('winter', 'WINTER'), ('fall', 'FALL')], default='summer', max_length=30)),
                ('areas', models.BooleanField()),
            ],
        ),
    ]
