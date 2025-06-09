from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from api.models import Servico
def loadIndexPage(request):
        return render(request, "index.html")


def loadCadastroPage(request):
        if request.method == 'GET':
            return render(request, 'cadastro.html')


def loadLoginPage(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(request, username= email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Login Efetuado com sucesso!")
            return redirect('indexPage')
        messages.error(request, 'Credenciais inválidas!')
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    
def loadCadastroServicePage(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            messages.warning(request, "Faça Login para acessar sua página de serviços!")
            return redirect('loginPage')
        
        return render(request, 'cadastroService.html') 
    

def loadMyServicesPage(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Faça Login para acessar sua página de serviços!")
        return redirect('loginPage')
    services = Servico.objects.filter(usuario=request.user.id)

    return render(request, 'myServices.html', {'services': services})

def loadSearchPage(request):
    if request.method == 'GET':
        services = Servico.objects.all()

        return render(request, 'search.html', {'services':services})


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('indexPage')