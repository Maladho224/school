# Generated by Django 5.0.6 on 2024-10-31 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0042_remove_devoir_date_aj_alter_userform_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='devoir',
            name='image',
            field=models.FileField(blank=True, max_length=50, null=True, upload_to='pdf'),
        ),
        migrations.AlterField(
            model_name='devoir',
            name='fichier',
            field=models.FileField(blank=True, null=True, upload_to='pdf'),
        ),
    ]
