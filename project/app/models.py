from django.db import models

# Create your models here.

class Contact(models.Model):
    Name=models.TextField()
    Email=models.EmailField()
    Phone=models.IntegerField()
    Alternative=models.TextField()
    Image=models.FileField()

    def __str__(self):
        return self.Name
    