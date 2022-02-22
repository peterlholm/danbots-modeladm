"Forms for trainingadm"
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import TrainingModel

class TestForm(forms.Form):
    tekst1 = forms.CharField(required=False, label='tekstfelt', max_length=50, strip=True)
    tekst2 = forms.CharField(required=False, label='tekstfelt2', max_length=50, strip=True)

class TrainingModelForm(forms.ModelForm):
    class Meta:
        model = TrainingModel
        exclude = ['']
    #     fields = ['description']

    def __init__(self, *args, **kwargs):
        #super(TrainingModelForm, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        #self.helper.wrapper_class = 'row'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-offset-1 col-lg-2'
        self.helper.field_class = 'col-lg-7'
        self.helper.add_input(Submit('submit', 'Send'))
        self.helper.add_input(Submit('cancel', 'Fortryd', css_class='btn-secondary', formnovalidate='formnovalidate', formaction='/'))


    # def __init__(self, *args, **kwargs):
    #     super(TrainingModelForm, self).__init__(*args, **kwargs)
    #     #super().__init__(*args, **kwargs)
    #     # self.helper = FormHelper()
    #     # self.helper.form_class = 'form-horizontal'
    #     # self.helper.label_class = 'col-sm-4'   # control-label
    #     # self.helper.field_class = 'col-sm-6'
    #     # self.helper.form_tag = True
    #     # self.helper.add_input(Submit('submit', 'Send'))
    #     # self.helper.add_input(Submit('cancel', 'Fortryd', css_class='btn-secondary', formnovalidate='formnovalidate', formaction='/'))
