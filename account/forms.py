from django.contrib.auth.forms import UserCreationForm

from account.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'phone')
