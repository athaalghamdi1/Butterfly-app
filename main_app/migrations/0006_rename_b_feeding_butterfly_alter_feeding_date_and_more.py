# Generated by Django 5.2 on 2025-04-10 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_feeding'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feeding',
            old_name='b',
            new_name='butterfly',
        ),
        migrations.AlterField(
            model_name='feeding',
            name='date',
            field=models.DateField(verbose_name='Feeding date'),
        ),
        migrations.AlterField(
            model_name='feeding',
            name='meal',
            field=models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner')], default='B', max_length=1),
        ),
    ]
