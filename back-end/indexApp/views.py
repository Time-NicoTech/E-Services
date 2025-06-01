from django.shortcuts import render, redirect
from django.contrib import messages

def loadIndexPage(request):
    if request.method == 'GET':
        return render(request, "index.html")


def loadCadastroPage(request):
    if request.method == 'POST':
        
        return redirect('loginPage')
    else:
        return render(request, 'cadastro.html')

def loadLoginPage(request):
    if request.method == 'POST':
        return render(request, 'index.html')
    else:
        return render(request, 'login.html')