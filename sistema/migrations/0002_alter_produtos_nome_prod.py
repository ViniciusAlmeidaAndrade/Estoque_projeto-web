# Generated by Django 5.1.2 on 2024-10-17 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='nome_prod',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]