# Generated by Django 5.0.6 on 2024-06-10 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messages_site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, verbose_name='Message de Mr/Mme')),
                ('e_mails', models.EmailField(max_length=30, verbose_name='E-mail')),
                ('message', models.TextField(verbose_name='Message')),
            ],
        ),
    ]
