from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length =100)
    image = models.ImageField(upload_to='postimages/')
    caption = models.TextField(blank=True)
    slug = models.SlugField(max_length=100,blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            
        super().save(*args,**kwargs)
