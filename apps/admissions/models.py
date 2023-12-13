from django.db import models
from slugify import slugify
from django.contrib.auth import get_user_model


User = get_user_model()

class AdmissionsPage(models.Model):

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, primary_key=True, blank=True)
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='user',
        related_name='admissions',
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = str(slugify(self.title))[:8]
        return super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Admissions'
        verbose_name_plural = 'Admissions'


class AdmissionsImage(models.Model):
    image = models.ImageField(upload_to='media/admissions_image')
    page = models.ForeignKey(
        to=AdmissionsPage,
        on_delete=models.CASCADE,
        related_name='admissions_images',
    )


class AdmissionsInfo(models.Model):

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, primary_key=True, blank=True)
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='user',
        related_name='admissions_info_user',
    )
    page = models.ForeignKey(
        to=AdmissionsPage,
        on_delete=models.CASCADE,
        related_name='admissions_info',
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = str(slugify(self.title))[:8]
        return super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Admissions'
        verbose_name_plural = 'Admissions'


class AdmissionsInfoImage(models.Model):
    image = models.ImageField(upload_to='media/admissions_image')
    info = models.ForeignKey(
        to=AdmissionsInfo,
        on_delete=models.CASCADE,
        related_name='admissions_info_images',
    )