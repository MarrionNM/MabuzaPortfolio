from django.db import models

# Create your models here.
 
class Person(models.Model):
    id = models.CharField(primary_key=True,max_length=100)
    name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, default="None")
    surname = models.CharField(max_length=50)
    profile_caption = models.CharField(max_length=50, default="None")
    email = models.CharField(max_length=100)
    cell = models.CharField(max_length=10)
    description = models.TextField(max_length=1000)
    
    image = models.ImageField(upload_to='profiles')

    def __str__(self):
        return self.name

class Project(models.Model):
    id = models.CharField(primary_key=True,max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='posters')
    
    trailer = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.title

class Platform(models.Model):
    id = models.CharField(primary_key=True,max_length=100)
    project = models.ForeignKey(Project, null=True, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    # description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='posters')

    def __str__(self):
        return self.name

class Social(models.Model):
    id = models.CharField(primary_key=True,max_length=100)
    person = models.ForeignKey(Person, null=True, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='posters')
    link = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
