# Generated by Django 3.2.7 on 2021-09-09 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainers_api', '0002_alter_tipopokemon_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='regiao',
        ),
        migrations.RemoveField(
            model_name='treinador',
            name='regiao',
        ),
        migrations.DeleteModel(
            name='Regiao',
        ),
    ]