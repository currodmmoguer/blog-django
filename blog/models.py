from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Almacena información sobre el blog
class Info(models.Model):
    key = models.CharField(max_length=30)
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.key.capitalize()

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = RichTextField(verbose_name="Contenido", null=True, blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    # Analítica
    visits = models.IntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
