from django import forms

from predio.models import Morador
from predio.models import Vaga
from predio.models import Carro
from predio.models import Visitante
from predio.models import PrestadorDeServico


class MoradorForm(forms.ModelForm):
    class Meta:
        model = Morador
        fields = ['CPF', 'nome', 'telefone', 'bloco', 'dataDeNascimento', 'numeroDoApartamento']


class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = ['numeroDaVaga', 'numeroDoApartamento']


class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ['modelo', 'cor', 'placa', 'numeroDaVaga']


class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = ['nome', 'dataDeNascimento', 'cpf', 'grauDeParentesco', 'numeroDoApartamento']


class PrestadorDeServicoForm(forms.ModelForm):
    class Meta:
        model = PrestadorDeServico
        fields = ['nome', 'rg', 'dataDeNascimento', 'nomeDaEmpresa', 'servico', 'numeroDoApartamento']
