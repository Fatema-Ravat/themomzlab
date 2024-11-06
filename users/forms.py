from django.forms import ModelForm
from django.admin.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [username,email,passwd1,passwd2]
