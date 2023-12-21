from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ExtendedUserCreationForm(UserCreationForm):
    # Добавляем дополнительные поля
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"sas"}), max_length=30, required=True, help_text='Обязательно. Введите свое имя.')
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"sas"}), max_length=30, required=True, help_text='Обязательно. Введите свою фамилию.')
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"sas"}), max_length=254, help_text='Обязательно. Введите корректную почту.')

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)