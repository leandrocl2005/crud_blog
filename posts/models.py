from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    autor=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    texto=models.TextField()
    pic=models.ImageField(upload_to='posts_pics',null=True,blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
	
    def __str__(self):
        return self.title+" by "+self.autor
