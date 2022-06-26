# Generated by Django 4.0.4 on 2022-06-09 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=30)),
                ('cor', models.CharField(max_length=100)),
                ('placa', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Morador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CPF', models.CharField(max_length=100)),
                ('nome', models.CharField(max_length=30)),
                ('telefone', models.CharField(max_length=100)),
                ('bloco', models.CharField(max_length=100)),
                ('dataDeNascimento', models.CharField(max_length=30)),
                ('numeroDoApartamento', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Predio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=30)),
                ('telefone', models.CharField(max_length=100)),
                ('qtdDeApartamento', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PrestadorDeServio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('rg', models.CharField(max_length=30)),
                ('dataDeNascimento', models.CharField(max_length=30)),
                ('nomeDaEmpresa', models.CharField(max_length=30)),
                ('servico', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroDaVaga', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Visitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('dataDeNascimento', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=100)),
                ('grauDeParentesco', models.CharField(max_length=100)),
            ],
        ),
    ]
