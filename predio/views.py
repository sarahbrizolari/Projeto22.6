from django.shortcuts import render, redirect

from predio.forms import MoradorForm
from predio.models import Morador

from predio.forms import VagaForm
from predio.models import Vaga

from predio.forms import CarroForm
from predio.models import Carro

from predio.forms import VisitanteForm
from predio.models import Visitante

from predio.forms import PrestadorDeServicoForm
from predio.models import PrestadorDeServico

#MORADOR --------
def list_Morador(request):
    Moradores = Morador.objects.all()
    return render(request, 'Morador.html', {'Moradores': Moradores})


def create_Morador(request):
    form = MoradorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_Morador')
    return render(request, 'Morador-form.html', {'form': form})


def update_Morador(request, id):
    Mor = Morador.objects.get(id=id)
    form = MoradorForm(request.POST or None, instance=Mor)
    if form.is_valid():
        form.save()
        return redirect('list_Morador')
    return render(request, 'Morador-form.html', {'form': form, 'Morador': Morador})


def delete_Morador(request, id):
    Mor = Morador.objects.get(id=id)
    if request.method == 'GET':
        Mor.delete()
        return redirect('list_Morador')
    return render(request, 'Morador-delete-confirm.html', {'Mor': Mor})

#VAGA----------
def list_Vaga(request):
    Vagas = Vaga.objects.all()
    return render(request, 'Vaga.html', {'Vagas': Vagas})


def create_Vaga(request):
    form = VagaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_Vaga')
    return render(request, 'Vaga-form.html', {'form': form})


def update_Vaga(request, id):
    Vag = Vaga.objects.get(id=id)
    form = VagaForm(request.POST or None, instance=Vag)
    if form.is_valid():
        form.save()
        return redirect('list_Vaga')
    return render(request, 'Vaga-form.html', {'form': form, 'Vaga': Vaga})


def delete_Vaga(request, id):
    Vag = Vaga.objects.get(id=id)
    if request.method == 'POST':
        Vag.delete()
        return redirect('list_Vaga')
    return render(request, 'Vaga-delete-confirm.html', {'Vag': Vag})

#CARRO---------
def list_Carro(request):
    Carros = Carro.objects.all()
    return render(request, 'Carro.html', {'Carros': Carros})


def create_Carro(request):
    form = CarroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_Carro')
    return render(request, 'Carro-form.html', {'form': form})


def update_Carro(request, id):
    Car = Carro.objects.get(id=id)
    form = CarroForm(request.POST or None, instance=Car)
    if form.is_valid():
        form.save()
        return redirect('list_Carro')
    return render(request, 'Carro-form.html', {'form': form, 'Carro': Carro})


def delete_Carro(request, id):
    Car = Carro.objects.get(id=id)
    if request.method == 'POST':
        Car.delete()
        return redirect('list_Carro')
    return render(request, 'Carro-delete-confirm.html', {'Car': Car})

#VISITANTE--------------
def list_Visitante(request):
    Visitantes = Visitante.objects.all()
    return render(request, 'Visitante.html', {'Visitantes': Visitantes})


def create_Visitante(request):
    form = VisitanteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_Visitante')
    return render(request, 'Visitante-form.html', {'form': form})


def update_Visitante(request, id):
    Vis = Visitante.objects.get(id=id)
    form = VisitanteForm(request.POST or None, instance=Vis)
    if form.is_valid():
        form.save()
        return redirect('list_Visitante')
    return render(request, 'Visitante-form.html', {'form': form, 'Visitante': Visitante})


def delete_Visitante(request, id):
    Vis = Visitante.objects.get(id=id)
    if request.method == 'POST':
        Vis.delete()
        return redirect('list_Visitante')
    return render(request, 'Visitante-delete-confirm.html', {'Vis': Vis})

#PRESTADOR DE SERVICO
def list_PrestadorDeServico(request):
    PrestadorDeServicos = PrestadorDeServico.objects.all()
    return render(request, 'PrestadorDeServico.html', {'PrestadorDeServicos': PrestadorDeServicos})


def create_PrestadorDeServico(request):
    form = PrestadorDeServicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_PrestadorDeServico')
    return render(request, 'PrestadorDeServico-form.html', {'form': form})


def update_PrestadorDeServico(request, id):
    Pres = PrestadorDeServico.objects.get(id=id)
    form = PrestadorDeServicoForm(request.POST or None, instance=Pres)
    if form.is_valid():
        form.save()
        return redirect('list_PrestadorDeServico')
    return render(request, 'PrestadorDeServico-form.html', {'form': form, 'PrestadorDeServico': PrestadorDeServico})


def delete_PrestadorDeServico(request, id):
    Pres = PrestadorDeServico.objects.get(id=id)
    if request.method == 'POST':
        Pres.delete()
        return redirect('list_PrestadorDeServico')
    return render(request, 'PrestadorDeServico-delete-confirm.html', {'Pres': Pres})
