from django.db import models

# Create your models here.
class place (models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

class Packages(models.Model):
    image=models.ImageField(upload_to='package/%D/%M/%Y')
    Date=models.DateField(auto_now=False)
    package_name=models.CharField(max_length=100)
    Company_name=models.CharField(max_length=100)
    package_desc=models.TextField()
    Discound_percentage = models.IntegerField()

