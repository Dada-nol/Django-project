# Generated by Django 5.0.6 on 2024-07-17 17:42

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bibliothecaire_app', '0011_remove_cd_membres_remove_empruntcd_cd_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('disponible', models.BooleanField(default=True)),
                ('artiste', models.CharField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dvd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('disponible', models.BooleanField(default=True)),
                ('realisateur', models.CharField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Emprunteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('NbEmprunt', models.IntegerField(default=0)),
                ('bloque', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='JeuDePlateau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('createur', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='EmpruntDvd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateEmprunt', models.DateField(default=datetime.date.today)),
                ('dateEmprunt_max', models.DateField(default=datetime.date(2024, 7, 24))),
                ('dvd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliothecaire_app.dvd')),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliothecaire_app.emprunteur')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmpruntCd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateEmprunt', models.DateField(default=datetime.date.today)),
                ('dateEmprunt_max', models.DateField(default=datetime.date(2024, 7, 24))),
                ('cd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliothecaire_app.cd')),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliothecaire_app.emprunteur')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='dvd',
            name='membres',
            field=models.ManyToManyField(related_name='dvds', through='bibliothecaire_app.EmpruntDvd', to='bibliothecaire_app.emprunteur'),
        ),
        migrations.AddField(
            model_name='cd',
            name='membres',
            field=models.ManyToManyField(related_name='cds', through='bibliothecaire_app.EmpruntCd', to='bibliothecaire_app.emprunteur'),
        ),
        migrations.CreateModel(
            name='EmpruntLivre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateEmprunt', models.DateField(default=datetime.date.today)),
                ('dateEmprunt_max', models.DateField(default=datetime.date(2024, 7, 24))),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliothecaire_app.emprunteur')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('disponible', models.BooleanField(default=True)),
                ('auteur', models.CharField(max_length=150)),
                ('membres', models.ManyToManyField(related_name='livres', through='bibliothecaire_app.EmpruntLivre', to='bibliothecaire_app.emprunteur')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='empruntlivre',
            name='livre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliothecaire_app.livre'),
        ),
    ]
