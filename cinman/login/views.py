from django.shortcuts import render

def login(request):
     return render(request, 'login/login_page.html')

def success(request):
     return render(request, 'login/success.html')
