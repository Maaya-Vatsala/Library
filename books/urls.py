#fichier servant à impoter les f et vues pour l'appli "books"

from django.urls import path
from .import views

app_name='books' #chaque url sera unique en indiquant zrfzrfs:index

#quand user accède URL racine (books), la vue index du module view sera appelée
urlpatterns = [
    #path('', views.books, name='index'), #url racine
    path('add/', views.addBook, name='addBook'), #url pour ajouter un livre donc écrire add
    path('', views.findBook, name = 'index'), #url racine car affiche sur la home page
    path('del/', views.Book_to_del, name = 'findBook'), #choisir un liv à supp pointer vers book_to_del
    path('history/', views.history, name = 'history'), #url pour afficher l'historique
    path('del/<int:b_id>/', views.delBook, name = 'delBook'), #url pour le liv choisi
]