# Generated by Django 5.1.2 on 2024-10-28 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visita_tecnico', '0005_relatoriosvisitas_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='relatoriosvisitas',
            name='nom_tecnico_f',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
