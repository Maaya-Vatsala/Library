from django.db import models

# Create your models here.

#là c un book (1 livre) pas l'ensemble attention

class Book(models.Model): #héritage de la classe Model de Django
    title = models.CharField(max_length = 100)  
    author = models.CharField(max_length = 100)
    date = models.IntegerField()

#historique livre supp
class DelBook(models.Model) :
    Reasons = [
        ("sold", "Sold"), #chaque partie doit être une paire, 1er val enregistrée dans la base et la 2e affiché dans formul
        ("lost", "Lost"), 
        ("damaged", "Damaged"), 
        ("other", "Other"),
    ]

    title = models.CharField(max_length = 100)  
    author = models.CharField(max_length = 100)
    date = models.IntegerField()
    reason = models.CharField(max_length = 100, choices=Reasons)
    reason_details = models.CharField(max_length=200, blank=True) #le vide accepté, facultatif sinon Dja demande précision meme motif pas "Other"
    del_date = models.DateTimeField(auto_now_add=True) #automatique bool