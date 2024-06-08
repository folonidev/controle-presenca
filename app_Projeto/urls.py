from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('update-presence/<int:aluno_id>/', views.update_presence, name='update_presence'),
    path('alunos/', views.lista_alunos, name='lista_alunos'),
    path('alunos/adicionar/', views.adicionar_aluno, name='adicionar_aluno'),
    path('alunos/editar/<int:pk>/', views.editar_aluno, name='editar_aluno'),
    path('alunos/excluir/<int:pk>/', views.excluir_aluno, name='excluir_aluno'),
    path('visualizar-presenca/', views.visualizar_presenca, name='visualizar_presenca'),
    path('visualizar-presenca/<int:data_filtro>/', views.visualizar_presenca, name='visualizar_presenca'),
]