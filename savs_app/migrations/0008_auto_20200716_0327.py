# Generated by Django 3.0.6 on 2020-07-16 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('savs_app', '0007_auto_20200716_0318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anonymouscomplaint',
            old_name='complaint_connection_unicamp',
            new_name='complainer_connection_unicamp',
        ),
        migrations.RenameField(
            model_name='anonymouscomplaint',
            old_name='complaint_connection_unicamp_complement',
            new_name='complainer_connection_unicamp_complement',
        ),
        migrations.RenameField(
            model_name='anonymouscomplaint',
            old_name='complaint_gender',
            new_name='complainer_gender',
        ),
        migrations.RenameField(
            model_name='anonymouscomplaint',
            old_name='complaint_gender_complement',
            new_name='complainer_gender_complement',
        ),
        migrations.RenameField(
            model_name='anonymouscomplaint',
            old_name='complaint_position',
            new_name='complainer_position',
        ),
        migrations.RenameField(
            model_name='anonymouscomplaint',
            old_name='complaint_position_complement',
            new_name='complainer_position_complement',
        ),
        migrations.RenameField(
            model_name='anonymouscomplaint',
            old_name='complaint_support_requested',
            new_name='complainer_support_requested',
        ),
        migrations.RenameField(
            model_name='anonymouscomplaint',
            old_name='complaint_support_requested_complement',
            new_name='complainer_support_requested_complement',
        ),
        migrations.RenameField(
            model_name='anonymouscomplaint',
            old_name='complaint_why_anonymous',
            new_name='complainer_why_anonymous',
        ),
        migrations.RenameField(
            model_name='envolvedperson',
            old_name='connecton_with_unicamp',
            new_name='person_connecton_with_unicamp',
        ),
        migrations.RenameField(
            model_name='envolvedperson',
            old_name='institute',
            new_name='person_institute',
        ),
        migrations.RenameField(
            model_name='envolvedperson',
            old_name='name',
            new_name='person_name',
        ),
        migrations.RenameField(
            model_name='envolvedperson',
            old_name='relationship_with_victim',
            new_name='person_relationship_with_victim',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complaint_address',
            new_name='complainer_address',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complaint_city',
            new_name='complainer_city',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complaint_connection_unicamp',
            new_name='complainer_connection_unicamp',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complaint_connection_unicamp_complement',
            new_name='complainer_connection_unicamp_complement',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complaint_course',
            new_name='complainer_course',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complaint_cpf',
            new_name='complainer_cpf',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complaint_email',
            new_name='complainer_email',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complaint_gender',
            new_name='complainer_gender',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complaint_gender_complement',
            new_name='complainer_gender_complement',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complaint_institute',
            new_name='complainer_institute',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complaint_is_social_name',
            new_name='complainer_is_social_name',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complaint_name',
            new_name='complainer_name',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complaint_neighborhood',
            new_name='complainer_neighborhood',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complaint_position',
            new_name='complainer_position',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complaint_position_complement',
            new_name='complainer_position_complement',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complaint_ra',
            new_name='complainer_ra',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complaint_state',
            new_name='complainer_state',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complaint_telephone',
            new_name='complainer_telephone',
        ),
        migrations.RenameField(
            model_name='identifiedcomplaint',
            old_name='complaint_zipcode',
            new_name='complainer_zipcode',
        ),
    ]
