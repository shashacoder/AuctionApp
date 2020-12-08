from django import forms
from django.contrib.auth.forms import UserCreationForm

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)