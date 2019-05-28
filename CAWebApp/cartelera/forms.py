from dal import autocomplete, forward
from .models import fechaCalendario, CategoryStudy, etiquetasCar
from django import forms


class fechaCalendarioForm(forms.ModelForm):

    class Meta:
        model = fechaCalendario
        fields = ('fechaCa', )
        # widgets = {
        #     'fechaCalendario': autocomplete.ModelSelect2Multiple(
        #         url='linked_data_rf',
        #         forward=(forward.Field(src="cat_estudio", dst="possessor"),
        #                  forward.Const(val=42, dst="secret"))
        #     )
        # }

# Etiquetas Cartelera
class EtiquetasCartForm(forms.ModelForm):

    class Meta:
        model = etiquetasCar
        fields = ('name', 'cat_estudio')
        widgets = {
            'cat_estudio': autocomplete.ModelSelect2Multiple(
                # url='linked_data_rf',
                forward=(forward.Field(src="cat_estudio", dst="possessor"),
                         forward.Const(val=42, dst="secret"))
            )
        }

class AutocompleteEtiquetasForm(forms.ModelForm):

    class Meta:
        model = etiquetasCar
        fields = ('__all__')
        widgets = {
            'etiquetasCartelera': autocomplete.ModelSelect2Multiple(
            'etiquetasCartelera-autocomplete'
            )
        }