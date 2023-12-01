"""appimoveis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from empreendimentos import views
from empreendimentos.views import reservar_unidade, detalhes_empreendimento, login_view, logout_view


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('cadastrar_empreendimento/', views.cadastrar_empreendimento, name='cadastrar_empreendimento'),
    path('lista_empreendimentos/', views.lista_empreendimentos, name='lista_empreendimentos'),
    # Cadastro de Unidades
    path('cadastrar_unidade/<int:empreendimento_id>/', views.cadastrar_unidade, name='cadastrar_unidade'),

    # Edição de Unidades
    path('editar_unidade/<int:unidade_id>/', views.editar_unidade, name='editar_unidade'),

    # Exclusão de Unidades
    path('excluir_unidade/<int:unidade_id>/', views.excluir_unidade, name='excluir_unidade'),

    # Listagem de Unidades
    path('listar_unidades/<int:empreendimento_id>/', views.listar_unidades, name='listar_unidades'),

    path('detalhes_empreendimento/<int:empreendimento_id>/reservar_unidade/', reservar_unidade, name='reservar_unidade'),
    path('detalhes_empreendimento/<int:empreendimento_id>/', detalhes_empreendimento, name='detalhes_empreendimento'),




]
    





