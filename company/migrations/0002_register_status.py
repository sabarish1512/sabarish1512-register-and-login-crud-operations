# Generated by Django 4.0.7 on 2024-08-19 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='Status',
            field=models.BooleanField(default=False),
        ),
    ]
