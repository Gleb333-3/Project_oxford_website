from django.db import models
from slugify import slugify
from django.contrib.auth import get_user_model

from datetime import datetime


User = get_user_model()

class News(models.Model):

    STATUS_CHOICES = (
        ('important', 'Important'),
        ('unimportant', 'Unimportant')
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, primary_key=True, blank=True)
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='user',
        related_name='news',
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug =  str(slugify(self.title))[:4] + str(datetime.now())[19:23]
        return super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


class NewsImage(models.Model):
    image = models.ImageField(upload_to='media/news_image')
    news = models.ForeignKey(
        to=News,
        on_delete=models.CASCADE,
        related_name='news_images',
    )