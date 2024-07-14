from django import forms
from .models import Book

class SaveBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['booktitle','bookdetail','bookauthor','bookimage','bookpath']