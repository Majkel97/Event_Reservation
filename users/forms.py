from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.', label= 'First name')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.', label= 'Last name')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', label= 'Email address')
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name','email')
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        helper = self.helper = FormHelper()

        # Moving field labels into placeholders
        layout = helper.layout = Layout()
        for field_name, field in self.fields.items():
            layout.append(Field(field_name, placeholder=field.label))
        helper.form_show_labels = False