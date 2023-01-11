from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
from ckeditor.fields import RichTextField

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
        
    category_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name
    
class Person(models.Model):
    genders = (
        ('M','Male'),
        ('F','Female')
    )
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.TextField(blank=True,null=True)
    image_url =  models.ImageField(upload_to='persons',blank=True,null=True)
    gender = models.CharField(max_length=1,choices=genders)
    duty = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Idea(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    target_amount = models.IntegerField()
    fund_amount = models.IntegerField()
    created_by = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    person = models.ManyToManyField(Person)
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    idea_image = models.ImageField(upload_to='images',blank=True,null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    


class Document(models.Model):
    title = models.CharField(max_length=100)
    document_url = models.FileField(upload_to="documents",blank=True,null=True)
    idea = models.ForeignKey(Idea,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.CharField(max_length=500)
    idea = models.ForeignKey(Idea,on_delete=models.CASCADE, related_name="comments")
    point = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.full_name}-({self.idea})"
    