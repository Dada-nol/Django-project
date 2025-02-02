# Generated by Django 5.0.6 on 2024-07-13 07:58

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliothecaire_app', '0002_rename_emprunteur_membre_rename_emprunteur_cd_membre_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cd',
            name='dateEmprunt',
        ),
        migrations.RemoveField(
            model_name='cd',
            name='membre',
        ),
        migrations.RemoveField(
            model_name='dvd',
            name='dateEmprunt',
        ),
        migrations.RemoveField(
            model_name='dvd',
            name='membre',
        ),
        migrations.RemoveField(
            model_name='livre',
            name='dateEmprunt',
        ),
        migrations.RemoveField(
            model_name='livre',
            name='membre',
        ),
        migrations.CreateModel(
            name='Emprunteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateEmprunt', models.DateField(default=datetime.datetime.now)),
                ('cd', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bibliothecaire_app.cd')),
                ('dvd', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bibliothecaire_app.dvd')),
                ('livre', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bibliothecaire_app.livre')),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliothecaire_app.membre')),
            ],
        ),
        migrations.AddField(
            model_name='cd',
            name='membres',
            field=models.ManyToManyField(through='bibliothecaire_app.Emprunteur', to='bibliothecaire_app.membre'),
        ),
        migrations.AddField(
            model_name='dvd',
            name='membres',
            field=models.ManyToManyField(through='bibliothecaire_app.Emprunteur', to='bibliothecaire_app.membre'),
        ),
        migrations.AddField(
            model_name='livre',
            name='membres',
            field=models.ManyToManyField(through='bibliothecaire_app.Emprunteur', to='bibliothecaire_app.membre'),
        ),
    ]
