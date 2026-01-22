from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
def logout_view(request):
    """Faz o logout do usário"""
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    """Faz o cadastro de um novo usuário."""
    if request.method != 'POST':
        # exibe o formulario do cadastro em branco
        form = UserCreationForm()
    else:
        # processa o formulario preenchidos
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()

        # Faz login do usuário e o redireciona para a página inicial

        authenticated_user = authenticate(username = new_user.username, password = request.POS['password1'])
        login(request= authenticated_user)
        return HttpResponseRedirect(reverse('index'))

    context = {'form': form}
    return render(request, 'user/register.html', context)