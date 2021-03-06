from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
from authentication.models import User


class Post(models.Model):
    content=models.TextField()
    image=models.ImageField(upload_to='posts',validators=[FileExtensionValidator[('png','jpd','jpeg')]])
    liked=models.ManyToManyField(User,default=None,related_name='likes')
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    def __str__(self):
        return str(self.content[:20])
    def num_likes(self):
        return self.liked.all().count()
    class Meta:
        ordering=('-created',)
class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    body=models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.pk)

LIKE_CHOICES=(
        ('Like','Like'),
        ('Unlike','Unlike')
)
class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    value=models.CharField(choices=LIKE_CHOICES,max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.user}-{self.post}-{self.user}"


