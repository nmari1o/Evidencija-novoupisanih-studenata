# Generated by Django 2.2.12 on 2022-12-13 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20221213_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email_studenta',
            field=models.EmailField(blank=True, max_length=70, unique=True),
        ),
    ]