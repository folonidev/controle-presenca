# myapp/admin.py
from django.contrib import admin
from .models import Aluno, Presenca

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'matricula')
    search_fields = ('nome', 'email', 'matricula')

@admin.register(Presenca)
class PresencaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'data', 'presente')
    list_filter = ('presente', 'data')
    search_fields = ('aluno__nome', 'aluno__email')
