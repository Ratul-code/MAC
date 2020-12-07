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

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)

    Name=models.CharField(max_length=50,default="")

    Email=models.CharField(max_length=50,default="")

    Phone=models.CharField(max_length=50,default="")

    Description=models.CharField(max_length=500,default="")

    def __str__(self):
        return self.Name



class Order(models.Model):
    order_id=models.AutoField(primary_key=True)

    item_json=models.CharField(max_length=50000,default="")

    name=models.CharField(max_length=90,default="")

    email=models.CharField(max_length=111,default="")

    address=models.CharField(max_length=111,default="")

    city=models.CharField(max_length=111,default="")

    state=models.CharField(max_length=111,default="")

    zip_code=models.CharField(max_length=111,default="")

    phone=models.CharField(max_length=111,default="")


    def __str__(self):
        return self.name


class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)

    order_id=models.IntegerField(default="")

    update_desc=models.CharField(max_length=5000)

    timestamp=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.update_desc[0:15] + "..."



