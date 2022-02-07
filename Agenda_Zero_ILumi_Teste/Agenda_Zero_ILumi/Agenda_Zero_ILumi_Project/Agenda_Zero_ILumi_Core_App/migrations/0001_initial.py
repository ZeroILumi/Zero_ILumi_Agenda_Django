# Generated by Django 3.2.8 on 2021-10-12 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento_Agendado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_do_evento_agendado', models.CharField(max_length=100)),
                ('decricao_do_evento_agendado', models.TextField(blank=True, null=True)),
                ('data_do_evento_agendado', models.DateTimeField()),
                ('data_da_criacao_do_evento_agendado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Eventos Agendados',
            },
        ),
    ]