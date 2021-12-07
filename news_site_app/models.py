from django.db import models

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=255)
  byline = models.CharField(max_length=255, null=True, blank=True)
  abstract = models.TextField()
  image = models.CharField(max_length=255, null=True, blank=True)
  created_date = models.DateTimeField(auto_now_add=True)
  section = models.CharField(max_length=20, null=True, blank=True)


  def __str__(self):
    return f"""
      Title: {self.title}
    """