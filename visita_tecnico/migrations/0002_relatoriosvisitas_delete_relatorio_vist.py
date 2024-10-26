# Generated by Django 5.1.2 on 2024-10-26 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visita_tecnico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatoriosVisitas',
            fields=[
                ('id_visita', models.AutoField(primary_key=True, serialize=False)),
                ('nom_tecnico', models.CharField(max_length=150)),
                ('nom_cliente', models.CharField(max_length=150)),
                ('endereco', models.CharField(max_length=250)),
                ('data', models.DateField(blank=True)),
                ('prod_usado', models.CharField(max_length=255)),
                ('observacoes', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Relatorio_vist',
        ),
    ]
