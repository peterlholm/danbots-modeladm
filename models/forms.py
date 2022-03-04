"Forms for trainingadm"
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import TrainingModel, SimulationModel

class TrainingModelForm(forms.ModelForm):
    class Meta:
        model = TrainingModel
        exclude = ['hostname', 'optimizer']
        #fields = ['date', 'description', 'model_path','sim_seen_score','sim_unseen_score','wand_score']

    def __init__(self, *args, **kwargs):
        #super(TrainingModelForm, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        #self.helper.wrapper_class = 'row'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-offset-2 col-lg-3'
        self.helper.field_class = 'col-lg-7'
        self.helper.add_input(Submit('submit', 'Save'))
        self.helper.add_input(Submit('cancel', 'Fortryd', css_class='btn-secondary', formnovalidate='formnovalidate', formaction='/models/trainlist'))

class SimulationModelForm(forms.ModelForm):
    class Meta:
        model = SimulationModel
        exclude = ['hostname', 'optimizer']
        #fields = ['date', 'description', 'model_path','sim_seen_score','sim_unseen_score','wand_score']

    def __init__(self, *args, **kwargs):
        #super(TrainingModelForm, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        #self.helper.wrapper_class = 'row'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-offset-2 col-lg-3'
        self.helper.field_class = 'col-lg-7'
        self.helper.add_input(Submit('submit', 'Save'))
        self.helper.add_input(Submit('cancel', 'Fortryd', css_class='btn-secondary', formnovalidate='formnovalidate', formaction='/models/simlist'))
