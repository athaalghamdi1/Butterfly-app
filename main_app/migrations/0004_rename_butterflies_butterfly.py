# Generated by Django 5.2 on 2025-04-09 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_butterflies_age_butterflies_wingspan'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='butterflies',
            new_name='butterfly',
        ),
    ]
