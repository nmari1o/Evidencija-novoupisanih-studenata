# Generated by Django 2.2.12 on 2022-12-13 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20221213_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email_studenta',
        ),
    ]
