from django.forms import ModelForm, Form, FileField
from django.forms.widgets import TextInput
from .models import Supplement, Category, Neurotransmitter


class SupplementForm(ModelForm):
    
    class Meta:
        model = Supplement
        exclude = ('slug',)


class SupplementImportForm(Form):
    file = FileField(
        label='Select a file',
    )


class CategoryForm(ModelForm):
    
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
        }


class NeurotransmitterForm(ModelForm):
    
    class Meta:
        model = Neurotransmitter
        fields = '__all__'
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
        }
