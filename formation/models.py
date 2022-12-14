from django.db import models


class Diplome(models.Model):
    diplome=models.CharField(max_length=50)
    datefin=models.DateField()
    Type=models.ForeignKey('Type',on_delete=models.CASCADE)
    def __str__(self) :
        return self.diplome
class Type(models.Model):
    TypeName = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self) :
        return self.TypeName  
class Skills(models.Model):
    skills=models.CharField(max_length=15)
    prec=models.IntegerField()
class Experience(models.Model):
    experience=models.CharField(max_length=20)
    datedebut=models.DateField()
    datefin=models.DateField()