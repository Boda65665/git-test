# Generated by Django 3.2.6 on 2021-12-20 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0016_auto_20211218_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='username',
            field=models.CharField(default=models.CharField(max_length=30), max_length=30),
        ),
    ]