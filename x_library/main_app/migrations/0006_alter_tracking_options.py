# Generated by Django 4.2 on 2023-05-04 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_workout_exercises'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tracking',
            options={'ordering': ('-date',)},
        ),
    ]
