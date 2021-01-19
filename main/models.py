from django.db import models

# Create your models here.
class user(models.Model):
    bank = models.CharField(max_length=50)
    pay = models.CharField(max_length=50)
    card_image = models.ImageField(upload_to='images')
    pay_image = models.ImageField(upload_to='images')
    limits = models.TextField()
    def __str__(self):
        return self.bank
    
'''    
class choice(models.Model):
    MERCHANT_KIND= (
        ('c', 'convenientstore'),
        ('d', 'drugstore'),
        ('s', 'shoppingmall'),

    )
    
    merchant = models.CharField(max_length=1, choices=MERCHANT_KIND)
    name = models.CharField(max_length=50)
   ''' 