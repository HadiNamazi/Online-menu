from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50)
    primary_price = models.IntegerField()
    secondary_price = models.IntegerField()
    image = models.ImageField(upload_to ='item_images/')
    description = models.TextField()
    rate = models.FloatField()
    likes = models.IntegerField()
    status = models.CharField(max_length=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name