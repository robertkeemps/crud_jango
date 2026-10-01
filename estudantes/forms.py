# app - forms.py file new

from django import forms
from .models import Estudante


class EstudanteForm(forms.ModelForm):

  class Meta:
    model = Estudante
    fields = (
        'nome',
        'foto',
        'email',
        'senha',
        'numero_celular',
        'data_de_nascimento',
    )

  def __init__(self, *args, **kwargs):
    super(EstudanteForm, self).__init__(*args, **kwargs)
    for visible in self.visible_fields():
      visible.field.widget.attrs['class'] = 'form-control'