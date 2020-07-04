from django.db.models import Q
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length = 30)

    def get_absolute_url(self):
        return reverse('post-list', kwargs={'pk':self.pk})

    def __str__(self):
        return f" {self.id}  {self.title} "

class Comment(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey("Post", on_delete=models.CASCADE,
                            related_name='comments')
    approve_comment = models.BooleanField(default=False)
    def approve(self):
        self.approve_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.content

# class PostManager(models.Model):

#     def search(self,query):
#         lookups = (Q(title__icontains=query)|
#                     Q(overview__icontains=query)|
#                     Q(author__icontains=query)
#         )
#         return self.get_queryset().filter(lookups).distinct()

class Post(models.Model):
    title = models.CharField(max_length=150)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add= True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    incredient_pdf = models.ImageField(blank=True, null=True)
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    likes = models.ManyToManyField(User, related_name='likes', blank=True, null=True)
    unlikes = models.ManyToManyField(User,related_name='unlikes',blank=True, null=True)

    #objects = PostManager()

    def total_unlikes(self):
        return self.unlikes.all().count()

    def total_likes(self):
        return self.likes.all().count()

    def __str__(self):
        return self.title

    def get_absolute_url(self, **kwargs):
        return reverse('post-detail', kwargs={
            'pk':self.pk
        })
    def get_category_count(self):
        return self.categories.all().count()

    def approve_comments(self):
        return self.comments.filter(approve_comment=True)

    def comment_count(self):
        return Comment.objects.filter(post=self).count()



