# Generated by Django 4.2 on 2023-04-04 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comptable', '0004_rename_libelle_comptegeneral_intitule_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='prefixe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comptable.journal'),
        ),
        migrations.DeleteModel(
            name='CodeJournal',
        ),
    ]