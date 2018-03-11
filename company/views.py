from django.shortcuts import render, redirect
from .forms import Compform
from .models import coforms


def com_form(request):
    form = Compform()
    if request.method == 'POST':
        form = Compform(request.POST)
        if form.is_valid():
            obj = coforms()
            obj.name = form.cleaned_data['name']
            obj.role = form.cleaned_data['role']
            obj.description = form.cleaned_data['description']
            obj.website = form.cleaned_data['website']
            obj.save()
            return render(request, 'homepage.html', {'form' : form})

    return render(request, 'compform.html', {'form' : form})