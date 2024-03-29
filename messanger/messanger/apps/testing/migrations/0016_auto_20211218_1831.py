# Generated by Django 3.2.6 on 2021-12-18 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0015_alter_info_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_friend', models.CharField(max_length=6)),
                ('id_chat', models.CharField(max_length=255)),
                ('id_create', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='info',
            name='image',
            field=models.ImageField(blank=True, default='media/imageses/prof_null.png', null=True, upload_to='imageses/'),
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_input', models.CharField(max_length=255)),
                ('text_message', models.CharField(max_length=255)),
                ('data_message', models.CharField(max_length=15)),
                ('id_chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.chats')),
            ],
        ),
    ]
