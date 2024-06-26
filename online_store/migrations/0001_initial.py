# Generated by Django 5.0.6 on 2024-06-21 20:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Categorie',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Couleur')),
            ],
            options={
                'verbose_name': 'Couleur',
                'verbose_name_plural': 'Couleurs',
            },
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopper_name', models.CharField(max_length=60, verbose_name='Nom du client')),
                ('number', models.IntegerField(verbose_name='Numéro de téléphone(8 caracteres)')),
                ('adresse', models.CharField(max_length=50, verbose_name='Lieu de résidence')),
                ('e_mail', models.EmailField(max_length=254, verbose_name='E_mail du destinataire')),
                ('name_and_quantity', models.CharField(max_length=50, verbose_name='Nom du produit')),
                ('montant', models.FloatField(default=1, verbose_name='Quantite')),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='online_store.color', verbose_name='Couleur')),
            ],
            options={
                'verbose_name': 'Commande',
                'verbose_name_plural': 'Commandes',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True, verbose_name='Nom')),
                ('price', models.FloatField(verbose_name='Prix')),
                ('quantity', models.IntegerField(default=1, verbose_name='Quantité')),
                ('description', models.TextField(default="la description de l'article ici", verbose_name='Description')),
                ('image', models.ImageField(null=True, upload_to='./img', verbose_name='image')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='online_store.category', verbose_name='categorie')),
            ],
            options={
                'verbose_name': 'Produit',
                'verbose_name_plural': 'Produits',
            },
        ),
        migrations.CreateModel(
            name='Panier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=23, verbose_name='Nom')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantite')),
                ('price', models.FloatField(verbose_name='Prix')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='online_store.products')),
            ],
        ),
    ]
