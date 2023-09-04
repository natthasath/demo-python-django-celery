from django.db import models
from .helpers import RandomFileName
import uuid

# Create your models here.
class article(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    publish = models.DateTimeField('publish')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self) :
        return self.title
    
    def cutbody(self) :
        return self.body[:255]+"..."
    
class photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to=RandomFileName('image'), verbose_name=u'อัพโหลดรูปภาพ')

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    def __str__(self):
        return str(self.image)