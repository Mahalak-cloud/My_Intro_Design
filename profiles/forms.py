from django import forms

class ProfileForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    profile_picture = forms.ImageField(required=False)
    resume = forms.FileField(required=False)