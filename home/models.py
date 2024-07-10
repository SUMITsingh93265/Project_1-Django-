from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=12)
    desc = models.TextField(null=True)
    date = models.DateField()

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=12)
    desc = models.TextField(null=True)

    def __str__(self):
        return self.name
    
class Ice_recipe(models.Model):
    ice_name = models.CharField(max_length=100)
    ice_discription = models.TextField()
    ice_image = models.ImageField(upload_to="ice_cream_pictures")