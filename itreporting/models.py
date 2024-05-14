from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

class Issue(models.Model):
    type = models.CharField(max_length = 100 , choices = [('Hardware', 'Hardware'), ('Software', 'Software')])
    room = models.CharField(max_length = 100)
    urgent = models.BooleanField(default = False)
    details = models.TextField()
    date_submitted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, related_name = 'issues', on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.type} Issue in {self.room}'

    def get_absolute_url(self):
        return reverse('itreporting:issue-detail', kwargs = {'pk': self.pk})
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

class UserProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)