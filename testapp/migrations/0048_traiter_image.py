# Generated by Django 5.0.6 on 2024-10-31 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0047_remove_devoir_num_devoir_traiter'),
    ]

    operations = [
        migrations.AddField(
            model_name='traiter',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='devoir'),
        ),
    ]
