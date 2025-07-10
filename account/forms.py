from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from account.models import CustomUser, Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'phone', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'phone', 'first_name', 'last_name')
        exclude = ('first_name', )


class ProfileChangeForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)
