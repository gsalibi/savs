# Generated by Django 3.0.6 on 2020-07-16 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savs_app', '0005_auto_20200716_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='anonymouscomplaint',
            name='complaint_why_anonymous',
            field=models.TextField(default=None),
        ),
    ]
