# Generated by Django 4.2 on 2023-04-04 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comptable', '0002_menu'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Societe',
            new_name='HistoriqueSociete',
        ),
    ]