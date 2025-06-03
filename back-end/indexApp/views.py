from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from api.models import Servico
def loadIndexPage(request):
    if request.method == 'GET':
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
            return redirect('loginPage')
        messages.error(request, 'Credenciais de usuário inválidos!')
        return render(request, 'index.html')
    else:
        return render(request, 'login.html')
    
def loadServicePage(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Faça Login para acessar sua página de serviços!")
        return redirect('loginPage')
    return render(request, 'cadastroService.html', {'user':request.user}) 

def loadSearchPage(request):
    if request.method == 'GET':
        services = Servico.objects.all()

        return render(request, 'search.html', {'services':services})


