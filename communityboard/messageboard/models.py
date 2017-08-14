from django.db import models
from django.template.defaultfilters import slugify


class Board(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True, blank=True, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Board, self).save(*args, **kwargs)


class Post(models.Model):
    board = models.ForeignKey(Board, related_name='posts')
    text = models.TextField()
    author = models.CharField(max_length=128, default='Anon')
    pinned = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Post made by {self.author} on {self.date_posted.isoformat()}'
