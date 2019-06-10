from django.contrib.auth.forms import UserCreationForm

from .models import User


class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email','first_name', 'last_name')
