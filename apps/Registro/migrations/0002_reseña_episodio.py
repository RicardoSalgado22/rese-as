# Generated by Django 5.0.6 on 2024-06-27 02:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reseña',
            name='episodio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Registro.episodio'),
        ),
    ]
