from django import forms 

class PostForm(forms.Form):
    owner=forms.IntegerField()
    description = forms.TextInput()
    _file = forms.FileInput()
    