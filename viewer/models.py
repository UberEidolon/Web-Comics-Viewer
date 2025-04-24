from django.db import models
from django.utils.text import slugify


class Manga(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    cover = models.ImageField(upload_to='manga_covers/')

    def __str__(self):
        return self.title

class Page(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='pages')
    image = models.ImageField(upload_to='manga_pages/')
    order = models.PositiveIntegerField()
    slug = models.SlugField(unique=False, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"page-{self.order}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.manga.title} — {self.slug}"
    