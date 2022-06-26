from django.db import models

class Morador(models.Model):
    CPF = models.CharField(max_length=100)
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=100)
    bloco = models.CharField(max_length=100)
    dataDeNascimento = models.CharField(max_length=30)
    numeroDoApartamento = models.CharField(max_length=100)

    def _str_(self):
        return self.CPF


class Vaga(models.Model):
    numeroDaVaga = models.CharField(max_length=100)
    numeroDoApartamento = models.CharField(max_length=100, null=True)

    def _str_(self):
        return self.numeroDaVaga


class Carro(models.Model):
    modelo = models.CharField(max_length=30)
    cor = models.CharField(max_length=100)
    placa = models.CharField(max_length=100)
    numeroDaVaga = models.CharField(max_length=100, null=True)

    def _str_(self):
        return self.modelo


class Visitante(models.Model):
    nome = models.CharField(max_length=30)
    dataDeNascimento = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    grauDeParentesco = models.CharField(max_length=100)
    numeroDoApartamento = models.CharField(max_length=100, null=True)


    def _str_(self):
        return self.nome


class PrestadorDeServico(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=30)
    dataDeNascimento = models.CharField(max_length=30)
    nomeDaEmpresa = models.CharField(max_length=30)
    servico = models.CharField(max_length=30)
    numeroDoApartamento = models.CharField(max_length=30, null=True)

    def _str_(self):
        return self.servico
