from django import forms
from .models import Book, DelBook #import, rend le modéle Book déf dans models.py

#crée un formu
class BookForm (forms.ModelForm):
    date = forms.IntegerField(label='Date', min_value=0, max_value=2027) #contrainte date

    class Meta: #Meta class interne pour def les champs
        model = Book
        fields = ['title', 'author', 'date']


#formulaire chercher un livre
class BookSearch(forms.Form) :
    title = forms.CharField(label = "Title", required= False) #required peut chercher avec seulement le titre, même si pas les autres infos
    author = forms.CharField(label = "Author", required = False)
    date = forms.IntegerField(label = "Date", required=False, min_value=0, max_value=2027)

#formulaire supp un livre
class BookDelete(forms.Form):
    reason = forms.ChoiceField(label = "Reason", choices=DelBook.Reasons)
    reason_det = forms.CharField(label="Details (optional)", required =False, max_length=200)
