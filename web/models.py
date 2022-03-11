from django.db import models
from versatileimagefield.fields import VersatileImageField

COLOR_CHOICES = (
    ("Red","Red"), ("Blue","Blue"), ("Yellow","Yellow"), ("Orange","Orange"),
)
SIZE_CHOICES = (
    ("42","42"), ("43","43"), ("44","44"), ("45","45"),
)


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,blank=True,null=True,unique=True)

    class Meta:
        ordering = ("-title","id")
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')

    def __str__(self):
        return f"{self.title}"


class Department(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ("-name","id")

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.PROTECT,blank=True,null=True)
    color = models.CharField(max_length=200,choices=COLOR_CHOICES)
    size = models.CharField(max_length=200,choices=SIZE_CHOICES)
    weight = models.CharField(max_length=200)
    photo = VersatileImageField()
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    mrp = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()
    description = models.TextField(blank=True,null=True)

    class Meta:
        ordering = ("-title","id")

    def __str__(self):
        return f"{self.title}"

        
class Customer(models.Model):
    first_name= models.CharField(max_length=30)
    last_name = models.CharField(max_length=20)
    email     = models.EmailField(unique=True)
    phone     = models.CharField(max_length=200)
    birth_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.name}"
        


class Order(models.Model):
    PAYMENT_STATUS_PENDING='P'
    PAYMENT_STATUS_COMPLETE='C'
    PAYMENT_STATUS_FAILED='F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING,'PENDING'),
        (PAYMENT_STATUS_COMPLETE,'COMPLETE'),
        (PAYMENT_STATUS_FAILED,'FAILED')
    ]
    placed_at=models.DateTimeField(auto_now_add=True)
    payment_status=models.CharField(max_length=200,choices=PAYMENT_STATUS_CHOICES,default=PAYMENT_STATUS_PENDING)

    def __str__(self):
        return f"{self.name}"


    


