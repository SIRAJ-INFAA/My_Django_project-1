# Generated by Django 5.0.6 on 2024-07-03 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subjectmarks',
            old_name='drama',
            new_name='acting',
        ),
        migrations.RenameField(
            model_name='subjectmarks',
            old_name='singing',
            new_name='dance',
        ),
    ]
