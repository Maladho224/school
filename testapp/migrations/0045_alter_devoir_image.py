# Generated by Django 5.0.6 on 2024-10-31 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0044_alter_devoir_fichier_alter_devoir_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devoir',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='devoir'),
        ),
    ]
