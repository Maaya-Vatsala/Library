# reçoit dmd, récup/enregi les livres, puis redigire vers la bonne page (donc vers templates html)

from .forms import BookForm, BookSearch, BookDelete #view importe le formulaire
from django.shortcuts import render, redirect, get_object_or_404 #render : pour aff template html ; redurect : pour rediriger vers une autre page
from .models import Book, DelBook #import, rend le modéle Book déf dans models.py 

# Create your views here.

#les fonctions

#1. recher un livre et aff livres trouvés -> vers index.html; recherche liv + lit formulaire + trie -> renvoie foru avec résu
#si pas seach, aff liste de toutes les oeuvres triées
#books (ensemble des livres)
def searchBook(request): #requete du user
    book_list = Book.objects.order_by("author", "title", "date") #plus all() = tous aff mais trier par ordre alphabé auteur, titre puis date publication (ex 2versions)
    form = BookSearch(request or None) #formulaire avec val saisies dans URL, Get = recherche (avoir ou ne pas avoir)
    search_performed = bool(request) #attention pas d'attribut get car son para request contient déjà GET car finBook l'appelle

    if form.is_valid() and search_performed: #respect forme du formu
        t = form.cleaned_data["title"] #récup val à verif avec ceux dans BookSearch
        a = form.cleaned_data["author"]
        d = form.cleaned_data["date"]

        if t : #si titre renseigné -> Djan filtre, garde oeuvres avec ce t
            book_list = book_list.filter(title__icontains = t) # attention 2 tirets du bas
        if a :
            book_list = book_list.filter(author__icontains = a)
        if d is not None: #car 0 =vide donc besoin d'être not None, si le champs vide alors None
            book_list= book_list.filter(date = d)

    return form, book_list


#2. gère la page, appelle searchBook + transmet for avec résu au template index.html pour aff
def findBook(request):
    form, book_list = searchBook(request.GET)
    return render(request, "books/index.html",{ #on déf le template qu'on veut affi ici un html-> index.html
        "form" : form,
        "books" : book_list,
        "search_performed" : bool(request.GET), #si trouvé alors true else false
    })


#2. ajouter un livre -> le lien vers le layout rediriger vers addBook.html
def addBook(request):
    if request.method == "POST": #formulaire vient d'être send par user
        form = BookForm(request.POST) #donne val saisies à Django

        if form.is_valid(): 
            form.save()  #sauvegarde le livre dans BD
            return redirect('books:index')  #redir page d'accueil après add
        
    else:
        form = BookForm()  #crée un formulaire vierge

    return render(request, 'books/addBook.html', {
            "form": form,
    })


#3. trouver livre à supp (il faut existe) + aff résu
def Book_to_del (request):
    form, book_list = searchBook(request.GET)
    return render(request, "books/delSearch.html", {
        "form" : form,
        "books" : book_list,
        "search_performed" : bool(request.GET),
    })

#4. supp un livre
def delBook(request, b_id):
    b = get_object_or_404(Book, id=b_id) #cherche modèle book

    if request.method == "POST":
        f= BookDelete(request.POST)

        if f.is_valid():
            DelBook.objects.create(
                title =b.title,
                author = b.author,
                date = b.date, 
                reason = f.cleaned_data["reason"],
                reason_details= f.cleaned_data["reason_det"],
            )
            b.delete()
            return redirect("books:history")
    else :
        f = BookDelete()

    return render(request, "books/delBook.html",{
        "book" : b,
        "form" : f,
    })

#5. historique trié par date de suppression
def history(request):
    list_del_books = DelBook.objects.order_by("-del_date")
    return render(request, "books/history.html",{
        "books" : list_del_books,
    })