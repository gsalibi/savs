# Generated by Django 3.0.8 on 2020-07-20 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savs_app', '0023_auto_20200719_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='anonymouscomplaint',
            name='anonymous_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='anonymouscomplaint',
            name='anonymous_current_status',
            field=models.TextField(choices=[('Atendimento não iniciado', 'Atendimento não iniciado'), ('Em andamento', 'Em andamento'), ('Atendimento finalizado', 'Atendimento finalizado'), ('Aguardando retorno', 'Aguardando retorno'), ('Invalida', 'Invalida')], default=None, null=True),
        ),
        migrations.AddField(
            model_name='anonymouscomplaint',
            name='anonymous_updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='identifiedcomplaint',
            name='identified_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='identifiedcomplaint',
            name='identified_current_status',
            field=models.TextField(choices=[('Atendimento não iniciado', 'Atendimento não iniciado'), ('Em andamento', 'Em andamento'), ('Atendimento finalizado', 'Atendimento finalizado'), ('Aguardando retorno', 'Aguardando retorno'), ('Invalida', 'Invalida')], default=None, null=True),
        ),
        migrations.AddField(
            model_name='identifiedcomplaint',
            name='identified_updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
