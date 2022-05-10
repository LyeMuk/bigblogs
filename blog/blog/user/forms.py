from django import forms
from . models import Post,Userdb

class postform(forms.ModelForm):
    class Meta:
        model=Post
        fields="__all__"
class userform(forms.ModelForm):
    class Meta:
        model=Userdb
        fields="__all__"