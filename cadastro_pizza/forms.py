from django.forms import ModelForm, Textarea, TextInput, NumberInput, CheckboxSelectMultiple, MultipleChoiceField, ChoiceField, Select
from django.utils.translation import ugettext_lazy as _
from django.forms import inlineformset_factory

from .models import Pizza, Ingrediente, ValorPizza

PIZZA_SIZES = (
    (1, 'Broto'),
    (2, 'Grande')
)

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

ValorPizzaFormSet = inlineformset_factory(Pizza,
    ValorPizza,
    fields=('quantia', 'tamanho_pizza'),
    widgets={'quantia': TextInput(attrs={'class':'form-control'}), 'tamanho_pizza':Select(choices=PIZZA_SIZES, attrs={'class':'form-control'})},
    max_num=2)

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
            'tamanho_pizza': ChoiceField(widget=Select(attrs={'class':'selector'})),
        }

class CadastroIngredienteForm(ModelForm):

	class Meta:
		model = Ingrediente
		fields = ['nome', 'descricao']
		widgets = {
			'nome': TextInput(attrs={'class':'form-control'}),
			'descricao':Textarea(attrs={'rows':'5', 'class':'form-control'})
		}
