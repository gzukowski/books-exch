from django import forms
from .models import Book, Exchange

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'condition', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description', 'rows': 4}),
            'condition': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter condition description'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        
class ExchangeForm(forms.ModelForm):
    class Meta:
        model = Exchange
        fields = ['requester_book']
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ExchangeForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['requester_book'].queryset = Book.objects.filter(owner=user)
