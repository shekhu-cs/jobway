from django.shortcuts import render
from company.models import coforms
from django.db.models import Q
from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse



def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        details = coforms.objects.filter(name__icontains=q)
        details = coforms.objects.filter(role__icontains=q)

        return render(request, 'homepage.html',{'details': details, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')

def homepage(request):
    return render(request, 'homepage.html')


def results(request):
    data = coforms.objects.all()
    return render(request, 'jobresult.html', {'data': data})




