# Generated by Django 3.2.6 on 2021-12-18 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0014_alter_info_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='image',
            field=models.ImageField(blank=True, default='images/profil.png', null=True, upload_to='imageses/'),
        ),
    ]