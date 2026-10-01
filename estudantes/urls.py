from django.urls import path
from estudantes import views

urlpatterns = [
    path('', views.listarEstudantes, name='listagem'),
    path('adicionar/', views.adicionarEstudante, name='adicionar'),
    path('editar/<int:id>/', views.editarEstudante, name='editar'),
    path('deletar/<int:id>/', views.deletarEstudante, name='deletar'),
    path('visualizar/<int:id>/', views.visualizarEstudante, name='visualizar'),
]