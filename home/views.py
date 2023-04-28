from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home/welcome.html', {'today': date.today().strftime('%d/%m/%Y')})

@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {})