from django.db import models
class Registration(models.Model):
    usersno=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    contact=models.CharField(max_length=30)
    emailid=models.CharField(max_length=30)



class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='media/shop/images', default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
        msg_id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=50)
        email = models.CharField(max_length=70, default="")
        phone = models.CharField(max_length=70, default="")
        desc = models.CharField(max_length=500, default="")

        def __str__(self):
            return self.name
