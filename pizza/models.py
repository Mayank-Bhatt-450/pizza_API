from django.db import models

# Create your models here.

class pizza_model(models.Model):

    pizza_type_CHOICES = [
    ('regular', 'regular'),
    ('square', 'square')]
    pizza_type= models.CharField(max_length=7,choices=pizza_type_CHOICES,default='regular')
    pizza_size_choices=[('small', 'small'),
    ('medium','medium'),
    ('large','large'),]
    pizza_size=models.CharField(max_length=7,choices=pizza_size_choices,default='medium')
    toppings=models.CharField(max_length=300)
    def __str__(self):
        return self.pizza_type
