# Generated by Django 3.2.9 on 2021-11-23 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='last_name',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='name',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
    ]
