from django.shortcuts import render, redirect, get_object_or_404
from .models import Empreendimento, Unidade
from .forms import EmpreendimentoForm, UnidadeForm
from django.shortcuts import render
from .forms import ReservaUnidadeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'home.html')

def faq(request):
    return render(request, 'faq.html')


def cadastrar_empreendimento(request):
    if request.method == 'POST':
        form = EmpreendimentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empreendimentos')  # Redireciona para a página de listagem de empreendimentos
    else:
        form = EmpreendimentoForm()
    
    return render(request, 'cadastro_empreendimento.html', {'form': form})

@login_required
def lista_empreendimentos(request):
    empreendimentos = Empreendimento.objects.all()
    return render(request, 'lista_empreendimentos.html', {'empreendimentos': empreendimentos})

def cadastrar_unidade(request, empreendimento_id):
    empreendimento = get_object_or_404(Empreendimento, pk=empreendimento_id)

    if request.method == 'POST':
        form = UnidadeForm(request.POST)
        if form.is_valid():
            unidade = form.save(commit=False)
            unidade.empreendimento = empreendimento
            unidade.save()
            return redirect('detalhes_empreendimento', empreendimento_id=empreendimento.id)
    else:
        # Passe o objeto de empreendimento como valor inicial para o campo no formulário
        form = UnidadeForm(initial={'empreendimento': empreendimento})

    return render(request, 'cadastrar_unidade.html', {'empreendimento': empreendimento, 'form': form})


# View para editar uma unidade
def editar_unidade(request, unidade_id):
    unidade = get_object_or_404(Unidade, pk=unidade_id)

    if request.method == 'POST':
        form = UnidadeForm(request.POST, instance=unidade)
        if form.is_valid():
            form.save()
            return redirect('detalhes_empreendimento', empreendimento_id=unidade.empreendimento.id)
    else:
        form = UnidadeForm(instance=unidade)

    return render(request, 'editar_unidade.html', {'form': form, 'unidade': unidade})

# View para excluir uma unidade
def excluir_unidade(request, unidade_id):
    unidade = get_object_or_404(Unidade, pk=unidade_id)
    empreendimento_id = unidade.empreendimento.id

    if request.method == 'POST':
        unidade.delete()
        return redirect('detalhes_empreendimento', empreendimento_id=empreendimento_id)

    return render(request, 'excluir_unidade.html', {'unidade': unidade})

# View para listar todas as unidades de um empreendimento
@login_required
def listar_unidades(request, empreendimento_id):
    empreendimento = get_object_or_404(Empreendimento, pk=empreendimento_id)
    unidades = Unidade.objects.filter(empreendimento=empreendimento)
    
    return render(request, 'listar_unidades.html', {'empreendimento': empreendimento, 'unidades': unidades})

@login_required
def detalhes_empreendimento(request, empreendimento_id):

    #if request.method=='GET':
        empreendimento = get_object_or_404(Empreendimento, pk=empreendimento_id)
        unidades = Unidade.objects.filter(empreendimento=empreendimento)

        return render(request, 'detalhes_empreendimento.html', {'empreendimento': empreendimento, 'unidades': unidades})

@login_required
def reservar_unidade(request, empreendimento_id):
    empreendimento = get_object_or_404(Empreendimento, pk=empreendimento_id)
    unidades_disponiveis = Unidade.objects.filter(empreendimento=empreendimento, status='disponivel')

    if request.method == 'POST':
        form = ReservaUnidadeForm(empreendimento, request.POST)
        if form.is_valid():
            unidade_reservada = form.cleaned_data['unidade']
            # Certifique-se de que o usuário atual esteja associado à reserva
            unidade_reservada.reservado_por = request.user
            unidade_reservada.status = 'reservada'
            unidade_reservada.save()
            return redirect('detalhes_empreendimento', empreendimento_id=empreendimento.id)
    else:
        form = ReservaUnidadeForm(empreendimento)

    return render(request, 'detalhes_empreendimento.html', {'empreendimento': empreendimento, 'unidades': unidades_disponiveis, 'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('lista_empreendimentos')
        else:
            # Lógica para lidar com tentativas de login inválidas
            pass

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')