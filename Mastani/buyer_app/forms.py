from django import forms
from auth_user.models import CustomUser

class UpdateUser(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','no_telp','email']