# Generated by Django 5.0.6 on 2024-10-25 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0017_userform_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='userform',
            name='matieres',
            field=models.CharField(choices=[('maths', 'Maths'), ('physique', 'physique'), ('chimie', 'Chimie')], default='', max_length=50),
        ),
    ]
