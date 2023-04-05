# Generated by Django 4.2 on 2023-04-04 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comptable', '0003_rename_societe_historiquesociete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comptegeneral',
            old_name='libelle',
            new_name='intitule',
        ),
        migrations.RenameField(
            model_name='comptetiers',
            old_name='libelle',
            new_name='intitule',
        ),
        migrations.AlterField(
            model_name='comptegeneral',
            name='code',
            field=models.CharField(max_length=5, unique=True),
        ),
    ]