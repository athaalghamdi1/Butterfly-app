# Generated by Django 5.2 on 2025-04-10 08:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rename_butterflies_butterfly'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('meal', models.CharField(max_length=1)),
                ('b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.butterfly')),
            ],
        ),
    ]
