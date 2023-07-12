from django.db import models
from django.contrib.auth.models import User

class BookStore(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book_name=models.CharField(max_length=100)
    price=models.IntegerField()
    author=models.CharField(max_length=200)
    pic=models.ImageField(upload_to="images",null=True,blank=True)
    description=models.CharField(max_length=200)

    def __str__(self):
        return self.book_name

