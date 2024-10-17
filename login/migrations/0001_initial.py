# Generated by Django 5.1.2 on 2024-10-17 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id_prod', models.AutoField(primary_key=True, serialize=False)),
                ('nome_prod', models.CharField(max_length=150)),
                ('vlr_prod', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('qtnd_prod', models.IntegerField(default=0)),
                ('entrada_prod', models.DateField()),
                ('saida_prod', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
