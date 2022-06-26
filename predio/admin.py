from django.contrib import admin

from .models import Morador, Vaga, Carro, Visitante, PrestadorDeServico


# Register your models here.
admin.site.register(Morador)
admin.site.register(Vaga)
admin.site.register(Carro)
admin.site.register(Visitante)
admin.site.register(PrestadorDeServico)
