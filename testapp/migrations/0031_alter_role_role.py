# Generated by Django 5.0.6 on 2024-10-26 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0030_alter_role_role_alter_userform_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
