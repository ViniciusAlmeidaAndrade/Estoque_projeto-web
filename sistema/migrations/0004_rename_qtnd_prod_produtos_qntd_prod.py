# Generated by Django 5.1.2 on 2024-10-26 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_produtos_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produtos',
            old_name='qtnd_prod',
            new_name='qntd_prod',
        ),
    ]