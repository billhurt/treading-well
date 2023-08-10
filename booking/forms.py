from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class ContactForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = "./success"
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn bg-treadwell-secondary treadwell-tertiary high-school border-0'))

    name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'bg-treadwell treadwell-tertiary', 'style': 'border-color: #EAFADA'}), max_length=100)
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'bg-treadwell treadwell-tertiary', 'style': 'border-color: #EAFADA'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your message', 'class': 'bg-treadwell treadwell-tertiary', 'style': 'border-color: #EAFADA'}), label="", max_length=400)
    captcha = ReCaptchaField(label="", widget=ReCaptchaV2Checkbox())