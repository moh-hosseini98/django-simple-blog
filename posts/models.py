from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PostView(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey('Post',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username 

class Author(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):

        return self.user.username

class Category(models.Model):

    title = models.CharField(max_length=20) 

    def __str__(self):

        return self.title   


class Comment(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey('Post',related_name='comments',on_delete=models.CASCADE)

    def __str__(self):

        return self.user.username

class Post(models.Model):

    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    #comment_count = models.IntegerField(default=0)
    #view_count = models.IntegerField(default=0)

    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    category = models.ManyToManyField(Category)
    featured = models.BooleanField(default=False)


    def __str__(self):

        return self.title

    @property

    def comment_count(self):

        return Comment.objects.filter(post=self).count()    


    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()

    @property

    def get_comments(self):

        return self.comments.all().order_by('-timestamp')    




    

