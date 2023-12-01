from django import forms
from .models import Empreendimento
from .models import Unidade

class EmpreendimentoForm(forms.ModelForm):
    class Meta:
        model = Empreendimento
        fields = ['nome', 'descricao', 'tipo_empreendimento']


class UnidadeForm(forms.ModelForm):
    class Meta:
        model = Unidade
        fields = '__all__'


class ReservaUnidadeForm(forms.Form):
    def __init__(self, empreendimento, *args, **kwargs):
        super(ReservaUnidadeForm, self).__init__(*args, **kwargs)
        self.fields['unidade'].queryset = Unidade.objects.filter(empreendimento=empreendimento, status='disponivel')

    unidade = forms.ModelChoiceField(queryset=Unidade.objects.none(), empty_label=None)
