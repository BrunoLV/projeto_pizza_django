from django.forms import ModelForm, Textarea, TextInput, NumberInput, CheckboxSelectMultiple, MultipleChoiceField
from django.utils.translation import ugettext_lazy as _
from .models import Pizza, Ingrediente, ValorPizza

class CadastroPizzaForm(ModelForm):
    
    class Meta:
        model = Pizza
        fields = ['sabor', 'descricao', 'ingredientes']
        labels = {
            'sabor': _('Sabor:'),
            'descricao': _('Descrição:'),
            'ingredientes': _('Ingredientes:')
        }
        widgets = {
            'sabor': TextInput(attrs={'class':'form-control'}),
            'descricao': Textarea(attrs={'rows':'5', 'class':'form-control'}),
            'ingredientes': CheckboxSelectMultiple(),
        }

class CadastroValorPizza(ModelForm):

    class Meta:
        model = ValorPizza
        fields = ['quantia', 'tamanho_pizza']
        labels = {
            'quantia': _('Valor:'),
            'tamanho_pizza': _('Tamanho:')
        }
        widgets = {
            'quantia': TextInput(attrs={'class':'form-control'}),
            'tamanho_pizza': MultipleChoiceField(),
        }

class CadastroIngredienteForm(ModelForm):

	class Meta:
		model = Ingrediente
		fields = ['nome', 'descricao']
		widgets = {
			'nome': TextInput(attrs={'class':'form-control'}),
			'descricao':Textarea(attrs={'rows':'5', 'class':'form-control'})
		}
