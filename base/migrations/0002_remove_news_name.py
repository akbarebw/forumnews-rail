# Generated by Django 4.1.1 on 2022-12-14 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='name',
        ),
    ]
