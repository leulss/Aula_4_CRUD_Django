from django.shortcuts import render, redirect
from .models import Comidas, Faixas, Finalizacao
from .forms import AddListaOrd
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    comidas = Comidas.objects.all()
    faixas = Faixas.objects.all()
    finalizacao = Finalizacao.objects.all()
    if request.method == "POST":
        form = AddListaOrd(request.POST)
        if form.is_valid():
            Comidas.objects.create(nome=form.cleaned_data["nome"],
                                   nutriente=form.cleaned_data["nutriente"],
                                   cor=form.cleaned_data["cor"])
    else:
        form = AddListaOrd()
    return render(request,
                  "home.html",
                  context={
                      "comidas": comidas,
                      "faixas": faixas,
                      "finalizacao": finalizacao,
                      "form_comida": form,
                      "action_com": "Adicionar"
                  })


@login_required
def change_comida(request, id):
    comida = Comidas.objects.get(id=id)
    if request.method == "POST":
        form = AddListaOrd(request.POST)
        comida.nome = form.cleaned_data["nome"]
        comida.nutriente = form.cleaned_data["nutriente"]
        comida.cor = form.cleaned_data["cor"]
        comida.save()
        return redirect(home)
    return render(request,
                  "home.html",
                  context={
                      "comida": comida,
                      "action_com": "Atualizar"
                  })


@login_required
def delete_comida(request, id):
    comida = Comidas.objects.get(id=id)
    if request.method == "POST":
        comida.delete()
        return redirect(home)
    return render(request, "r_sure.html")


def create_faixa(request):
    if request.method == "POST":
        Faixas.objects.create(arte_marcial=request.POST["arte_marcial"],
                              cor=request.POST["cor"],
                              requer=request.POST["requer"])
        return redirect(home)
    return render(request, "form_faixa.html", context={"action": "Adicionar"})


@login_required
def create_finalizacao(request):
    if request.method == "POST":
        Finalizacao.objects.create(arte_marcial=request.POST["arte_marcial"],
                                   tipo=request.POST["tipo"],
                                   pontos=request.POST["pontos"])
        return redirect(home)
    return render(request,
                  "form_finalizacao.html",
                  context={"action": "Adicionar"})


@login_required
def change_faixa(request, id):
    faixas = Faixas.objects.get(id=id)
    if request.method == "POST":
        faixas.arte_marcial = request.POST["arte_marcial"]
        faixas.cor = request.POST["cor"]
        faixas.requer = request.POST["requer"]
        faixas.save()
        return redirect(home)
    return render(request,
                  "form_faixa.html",
                  context={
                      "faixa": faixas,
                      "action": "Atualizar"
                  })


@login_required
def delete_faixa(request, id):
    faixa = Faixas.objects.get(id=id)
    if request.method == "POST":
        faixa.delete()
        return redirect(home)
    return render(request, "r_sure.html")


@login_required
def change_finalizacao(request, id):
    finalizacao = Finalizacao.objects.get(id=id)
    if request.method == "POST":
        finalizacao.arte_marcial = request.POST["arte_marcial"]
        finalizacao.tipo = request.POST["tipo"]
        finalizacao.pontos = request.POST["pontos"]
        finalizacao.save()
        return redirect(home)
    return render(request,
                  "form_finalizacao.html",
                  context={
                      "finalizacao": finalizacao,
                      "action": "Atualizar"
                  })


@login_required
def delete_finalizacao(request, id):
    finalizacao = Finalizacao.objects.get(id=id)
    if request.method == "POST":
        finalizacao.delete()
        return redirect(home)
    return render(request, "r_sure.html")


def create_user(request):
    if request.method == "POST":
        user = User.objects.create_user(request.POST["username"],
                                        request.POST["email"],
                                        request.POST["password"])
        user.save()
        return redirect("home")
    return render(request, "register.html")


def login_user(request):
    if request.method == "POST":
        user = authenticate(username=request.POST["username"],
                            password=request.POST["password"])
        if user != None:
            login(request, user)
        else:
            return render(request,
                          "login.html",
                          context={"error_msg": "Usuário não pode logar"})
        if request.user.is_authenticated:
            return redirect('home')
    return render(request, "login.html",context={"error_msg": "Usuário não pode logar"})


def logout_user(request):
    logout(request)
    return redirect('login')
