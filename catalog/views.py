from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "contacts.html")


def contacts_post(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        email = request.POST.get('email')
        return HttpResponse(f'Введенные данные: {name}, {email}, {message}')
    return render(request, 'catalog/contacts.html')
