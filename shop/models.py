from django.db import models
# shop1234

# Create your models here.
class product(models.Model):
    product_id=models.AutoField

    product_name=models.CharField(max_length=50,default="")

    Product_category=models.CharField(max_length=50,default="")

    Product_subcategory=models.CharField(max_length=50,default="")

    product_desc=models.CharField(max_length=200,default="")

    product_price=models.IntegerField(default=0)

    pub_date=models.DateField()

    image=models.ImageField(upload_to="shop/image")


    def __str__(self):
        return self.product_name