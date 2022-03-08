"Forms for runqueue"
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import RunQueue

class RunQueueForm(forms.ModelForm):
    class Meta:
        model = RunQueue
        exclude = ['', '']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        #self.helper.wrapper_class = 'row'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-offset-2 col-lg-3'
        self.helper.field_class = 'col-lg-7'
        self.helper.add_input(Submit('submit', 'Save'))
        self.helper.add_input(Submit('cancel', 'Fortryd', css_class='btn-secondary', formnovalidate='formnovalidate', formaction='/models/trainlist'))
