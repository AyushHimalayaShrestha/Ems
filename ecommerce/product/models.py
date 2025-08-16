from django.db import models
from django.shortcuts import render
# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.category_name