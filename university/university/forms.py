# coding: utf-8
from university import models
from django import forms

class GroupsEdit(forms.Form):
    group_name=forms.CharField()
    person_number = forms.IntegerField()
    decan = forms.ModelChoiceField(queryset=models.Decan.objects.all())
    specialty = forms.ModelChoiceField(queryset=models.Specialy.objects.all())
    pisun = forms.ModelChoiceField(queryset=models.Pisun.objects.all())