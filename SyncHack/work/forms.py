from django import forms
from .models import UserProfile, Department


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile  
        fields = ['email', 'first_name', 'last_name', 'role', 'password']


class AddUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddUserForm, self).__init__(*args, **kwargs)
        self.fields['department'].queryset = Department.objects.all()

    class Meta:
        model = UserProfile
        fields = ['email', 'first_name', 'last_name', 'role', 'department', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }