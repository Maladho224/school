# Generated by Django 5.0.6 on 2024-10-26 02:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0024_alter_classes_classe_alter_ecole_ecoles_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matieres',
            name='matieres',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userform',
            name='matieres',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='testapp.matieres'),
        ),
        migrations.AlterField(
            model_name='userform',
            name='role',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='testapp.role'),
        ),
    ]
