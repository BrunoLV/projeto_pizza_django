from django.forms import ModelForm, Textarea, TextInput, NumberInput, CheckboxSelectMultiple
from .models import Pizza

class CadastroPizzaForm(ModelForm):
    class Meta:
        model = Pizza
        fields = '__all__'
        widgets = {
            'sabor': TextInput(attrs={'class':'form-control'}),
            'descricao': Textarea(attrs={'rows':'5', 'class':'form-control'}),
            'valor': NumberInput(attrs={'class':'form-control'}),
            'ingredientes': CheckboxSelectMultiple(attrs={'class':'form-control'}),
        }