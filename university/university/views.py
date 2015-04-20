from django.shortcuts import render, redirect
from university import forms
from university import  models

def home(request):
    context = {}
    context['hello'] = 'hello'
    return render (request,'home.html', context)

def groups_edit(request):
    context = {}

    form = forms.GroupsEdit(request.POST or None)
    if form.is_valid():
        student = models.Group.objects.create(
            group_name=form.cleaned_data.get('group_name'),
            person_number=form.cleaned_data.get('person_number'),
            decan=form.cleaned_data.get('decan'),
            specialty=form.cleaned_data.get('specialty'),
            pisun=form.cleaned_data.get('pisun')
        )
        return redirect(home)

    context['form'] = form
    return render(request, 'groups_edit.html', context)