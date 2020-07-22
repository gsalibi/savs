from django import forms

from .models import AnonymousComplaint, IdentifiedComplaint, EnvolvedPerson


class AnonymousComplaintForm(forms.ModelForm):
    class Meta:
        model = AnonymousComplaint
        fields = [
            'anonymous_position',
            'anonymous_position_complement',
            'anonymous_gender',
            'anonymous_gender_complement',
            'anonymous_connection_unicamp',
            'anonymous_connection_unicamp_complement',
            'anonymous_support_requested',
            'anonymous_support_requested_complement',
            'anonymous_why_anonymous',
            'anonymous_why_anonymous_complement',
            'anonymous_episode_date',
            'anonymous_episode_date_complement',
            'anonymous_episode_date_period',
            'anonymous_episode_date_period_complement',
            'anonymous_episode_location',
            'anonymous_episode_location_complement',
            'anonymous_episode_report'
        ]
        widgets = {
            'anonymous_position': forms.Select(attrs={"class": "form-control", "onchange": "displayOpenField(this, [4], 'id_anonymous_position_complement')"}),
            'anonymous_position_complement': forms.TextInput(attrs={"class": "form-control", "placeholder": "Qual", "style": "display: none;"}),
            'anonymous_gender': forms.Select(attrs={"class": "form-control", "onchange": "displayOpenField(this, [3], 'id_anonymous_gender_complement')"}),
            'anonymous_gender_complement': forms.TextInput(attrs={"class": "form-control", "placeholder": "Qual", "style": "display: none;"}),
            'anonymous_connection_unicamp': forms.Select(attrs={"class": "form-control", "onchange": "displayOpenField(this, [4], 'id_anonymous_connection_unicamp_complement')"}),
            'anonymous_connection_unicamp_complement': forms.TextInput(attrs={"class": "form-control", "placeholder": "Qual", "style": "display: none;"}),
            'anonymous_support_requested': forms.Select(attrs={"class": "form-control", "onchange": "displayOpenField(this, [0], 'id_anonymous_support_requested_complement')"}),
            'anonymous_support_requested_complement': forms.TextInput(attrs={"class": "form-control", "placeholder": "Qual"}),
            'anonymous_why_anonymous': forms.Select(attrs={"class": "form-control", "onchange": "displayOpenField(this, [4], 'id_anonymous_why_anonymous_complement')"}),
            'anonymous_why_anonymous_complement': forms.TextInput(attrs={"class": "form-control", "placeholder": "Qual", "style": "display: none;"}),
            'anonymous_episode_date': forms.Select(attrs={"class": "form-control", "onchange": "displayOpenField(this, [3], 'id_anonymous_episode_date_complement')"}),
            'anonymous_episode_date_complement': forms.TextInput(attrs={"class": "form-control", "placeholder": "dd/mm/aaaa", "style": "display: none;"}),
            'anonymous_episode_date_period': forms.Select(attrs={"class": "form-control", "onchange": "displayOpenField(this, [4], 'id_anonymous_episode_date_period_complement')"}),
            'anonymous_episode_date_period_complement': forms.TextInput(attrs={"class": "form-control", "placeholder": "hh:mm", "style": "display: none;"}),
            'anonymous_episode_location': forms.Select(attrs={"class": "form-control", "onchange": "displayOpenField(this, [4,5], 'id_anonymous_episode_location_complement')"}),
            'anonymous_episode_location_complement': forms.TextInput(attrs={"class": "form-control", "placeholder": "Onde, exatamente", "style": "display: none;"}),
            'anonymous_episode_report': forms.Textarea(attrs={"class": "form-control", "placeholder": "O que aconteceu? Inclua tudo o que for capaz de lembrar sobre o que vivenciou nesse episódio.", "rows": "6"}),
        }


class IdentifiedComplaintForm(forms.ModelForm):
    class Meta:
        model = IdentifiedComplaint
        fields = [
            'identified_position',
            'identified_position_complement',
            'identified_gender',
            'identified_gender_complement',
            'identified_name',
            'identified_cpf',
            'identified_is_social_name',
            'identified_zipcode',
            'identified_neighborhood',
            'identified_city',
            'identified_state',
            'identified_address',
            'identified_address_number',
            'identified_email',
            'identified_telephone',
            'identified_connection_unicamp',
            'identified_connection_unicamp_complement',
            'identified_institute',
            'identified_ra',
            'identified_course',
            'identified_episode_date',
            'identified_episode_date_complement',
            'identified_episode_date_period',
            'identified_episode_date_period_complement',
            'identified_episode_location',
            'identified_episode_location_complement',
            'identified_episode_report',
        ]
        widgets = {
            'identified_position': forms.Select(attrs={"class": "form-control", "onchange": "displayOpenField(this, [4], 'id_identified_position_complement')"}),
            'identified_position_complement': forms.TextInput(attrs={"class": "form-control", "placeholder": "Qual", "style": "display: none;"}),
            'identified_gender': forms.Select(attrs={"class": "form-control", "onchange": "displayOpenField(this, [3], 'id_identified_gender_complement')"}),
            'identified_gender_complement': forms.TextInput(attrs={"class": "form-control", "placeholder": "Qual", "style": "display: none;"}),
            'identified_connection_unicamp': forms.Select(attrs={"class": "form-control", "onchange": "displayOpenField(this, [4], 'id_identified_connection_unicamp_complement')"}),
            'identified_connection_unicamp_complement': forms.TextInput(attrs={"class": "form-control", "placeholder": "Qual", "style": "display: none;"}),
            'identified_support_requested': forms.Select(attrs={"class": "form-control", "onchange": "displayOpenField(this, [0], 'id_identified_support_requested_complement')"}),
            'identified_support_requested_complement': forms.TextInput(attrs={"class": "form-control", "placeholder": "Qual"}),
            'identified_why_anonymous': forms.Select(attrs={"class": "form-control", "onchange": "displayOpenField(this, [4], 'id_identified_why_identified_complement')"}),
            'identified_why_identified_complement': forms.TextInput(attrs={"class": "form-control", "placeholder": "Qual", "style": "display: none;"}),
            'identified_episode_date': forms.Select(attrs={"class": "form-control", "onchange": "displayOpenField(this, [3], 'id_identified_episode_date_complement')"}),
            'identified_episode_date_complement': forms.TextInput(attrs={"class": "form-control", "placeholder": "dd/mm/aaaa", "style": "display: none;"}),
            'identified_episode_date_period': forms.Select(attrs={"class": "form-control", "onchange": "displayOpenField(this, [4], 'id_identified_episode_date_period_complement')"}),
            'identified_episode_date_period_complement': forms.TextInput(attrs={"class": "form-control", "placeholder": "hh:mm", "style": "display: none;"}),
            'identified_episode_location': forms.Select(attrs={"class": "form-control", "onchange": "displayOpenField(this, [4,5], 'id_identified_episode_location_complement')"}),
            'identified_episode_location_complement': forms.TextInput(attrs={"class": "form-control", "placeholder": "Onde, exatamente", "style": "display: none;"}),
            'identified_episode_report': forms.Textarea(attrs={"class": "form-control", "placeholder": "O que aconteceu? Inclua tudo o que for capaz de lembrar sobre o que vivenciou nesse episódio.", "rows": "6"}),
            'identified_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Nome Completo"}),
            'identified_cpf': forms.TextInput(attrs={"class": "form-control", "placeholder": "CPF"}),
            'identified_is_social_name': forms.CheckboxInput(attrs={"class": "form-check-input"}),
            'identified_zipcode': forms.TextInput(attrs={"class": "form-control", "maxlength": "9", "placeholder": "CEP", "onblur": "cepSearch(this.value)"}),
            'identified_neighborhood': forms.TextInput(attrs={"type": "hidden"}),
            'identified_city': forms.TextInput(attrs={"type": "hidden"}),
            'identified_state': forms.TextInput(attrs={"type": "hidden"}),
            'identified_address': forms.TextInput(attrs={"type": "hidden"}),
            'identified_address_number': forms.TextInput(attrs={"class": "form-control", "placeholder": "nº"}),
            'identified_email': forms.TextInput(attrs={"class": "form-control", "placeholder": "E-mail"}),
            'identified_telephone': forms.TextInput(attrs={"class": "form-control", "placeholder": "Celular/Telefone"}),
            'identified_connection_unicamp': forms.Select(attrs={"class": "form-control", "onchange": "displayUniversityInfos()"}),
            'identified_institute': forms.TextInput(attrs={"class": "form-control", "placeholder": "Instituto/Faculdade/Órgão...", "list": "listInstitute"}),
            'identified_ra': forms.TextInput(attrs={"class": "form-control", "placeholder": "RA/Matrícula"}),
            'identified_course': forms.TextInput(attrs={"class": "form-control", "placeholder": "Curso...", "list": "listCourse"}),
            'identified_connection_unicamp_complement': forms.TextInput(attrs={"class": "form-control", "placeholder": "Vínculo", "style": "display: none;"}),
        }


class EnvolvedPersonForm(forms.ModelForm):
    class Meta:
        model = EnvolvedPerson
        fields = [
            'is_accused',
            'person_name',
            'person_connecton_unicamp',
            'person_connecton_unicamp_complement',
            'person_institute',
            'person_ra',
            'person_course',
            'person_relationship_victim',
            'person_information_complement'
        ]
