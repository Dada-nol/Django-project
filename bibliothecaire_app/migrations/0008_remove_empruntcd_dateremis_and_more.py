# Generated by Django 5.0.6 on 2024-07-13 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bibliothecaire_app', '0007_membre_nbemprunt_empruntcd_cd_membres_empruntdvd_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empruntcd',
            name='dateRemis',
        ),
        migrations.RemoveField(
            model_name='empruntdvd',
            name='dateRemis',
        ),
        migrations.RemoveField(
            model_name='empruntlivre',
            name='dateRemis',
        ),
    ]
