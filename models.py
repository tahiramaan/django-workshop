from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS=(
    (0,'Draft'),
    (1,'Publish')
)
class Post(models.Model):
    title=models.CharField(max_length=300,unique=True)
    slug=models.SlugField(max_length=300,unique=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    status=models.IntegerField(choices=STATUS,default=0)
    updated_on=models.DateTimeField(auto_now=True)
    content=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering=['-created_on']
    
    def __str__(self):
        return self.title
    