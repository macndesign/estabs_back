# Generated by Django 2.2.3 on 2019-07-16 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estabelecimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('logradouro', models.CharField(max_length=300, verbose_name='Logradouro')),
                ('numero', models.CharField(max_length=10, verbose_name='Número')),
                ('bairro', models.CharField(max_length=200, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=50, verbose_name='Estado')),
                ('lat', models.CharField(max_length=50, verbose_name='Estado')),
                ('lon', models.CharField(max_length=50, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Estabelecimento',
                'verbose_name_plural': 'Estabelecimentos',
                'ordering': ['nome'],
            },
        ),
    ]