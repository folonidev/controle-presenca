# Generated by Django 5.0.6 on 2024-05-15 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_Projeto', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['-date']},
        ),
    ]