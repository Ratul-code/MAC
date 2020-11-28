from django.db import models
# shop1234

# Create your models here.
class product(models.Model):
    product_id=models.AutoField

    Name=models.CharField(max_length=50,default="")

    Category=models.CharField(max_length=50,default="")

    Subcategory=models.CharField(max_length=50,default="")

    Description=models.CharField(max_length=200,default="")

    Price=models.IntegerField(default=0)

    pub_date=models.DateField()

    image=models.ImageField(upload_to="shop/image")


    def __str__(self):
        return self.Name