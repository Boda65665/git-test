# Generated by Django 3.2.6 on 2021-12-20 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0019_alter_info_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='username',
        ),
        migrations.AddField(
            model_name='info',
            name='usernames',
            field=models.CharField(default='Нетуc', max_length=30),
        ),
    ]
