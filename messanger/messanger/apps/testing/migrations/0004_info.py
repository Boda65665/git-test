# Generated by Django 3.2.6 on 2021-11-26 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0003_delete_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('pol', models.CharField(max_length=1)),
                ('year', models.CharField(max_length=4)),
                ('o_sebe', models.CharField(max_length=255)),
                ('ville', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=30)),
                ('user_prof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]