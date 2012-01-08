from django import forms
import re
from taggit.forms import TagField

class PostForm(forms.Form):
    title = forms.CharField(max_length=200)
    email = forms.EmailField()
    description = forms.CharField(max_length=4000)
    expires_on = forms.DateField()
    tags = TagField()
