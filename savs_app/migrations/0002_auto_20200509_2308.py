# Generated by Django 3.0.3 on 2020-05-09 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('savs_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_complaint', models.CharField(choices=[('DISCRI', 'Discriminação baseada em Gênero e/ou Sexualidade'), ('ASSALT', 'Assalto Sexual'), ('HARASS', 'Assédio Sexual'), ('ONLINE', 'Assédio Sexual Cibernético')], max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('ra', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=12)),
                ('university_bond', models.CharField(choices=[('UNDER', 'Aluna(o) de graduação'), ('GRADU', 'Aluna(o) de pós-graduação'), ('EMPLO', 'Funcionária(o)'), ('CONTR', 'Terceirizada(o)'), ('PROFE', 'Docente'), ('OTHER', 'Outro')], max_length=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='teste2',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Teste1',
        ),
        migrations.DeleteModel(
            name='Teste2',
        ),
        migrations.AddField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='savs_app.User'),
        ),
    ]
