# Generated by Django 5.1.2 on 2024-10-25 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Relatorio_vist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_tecnicos', models.CharField(max_length=50)),
                ('nom_clientes', models.CharField(max_length=50)),
                ('enderecos', models.CharField(max_length=150)),
                ('datas', models.DateField(auto_now_add=True, verbose_name='')),
                ('prod_usados', models.CharField(max_length=255)),
                ('observacoes', models.CharField(max_length=255)),
            ],
        ),
    ]
