from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=100)

class Post(models.Model):

    title=models.CharField(max_length=70)

    body=models.TextField()

    created_time=models.DateTimeField()

    modified_time=models.DateTimeField()

    category=models.ForeignKey(Category)

    tags=models.ManyToManyField(Tag,blank=True)

    author=models.ForeignKey(User)

    views=models.PositiveIntegerField(default=0)

    class Meta:
        ordering=["-created_time"]

    def __str__(self):
        return self.title

    #generate post url
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views+=1
        self.save(update_fields=['views'])
