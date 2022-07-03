from django.db import models

# Create your models here.class EBooksModel(models.Model):
class EBooksModel(models.Model):

    titlee = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=None, blank=True)
    year = models.CharField(max_length=100, null=None, blank=True)
    publisher = models.CharField(max_length=200, null=None, blank=True)
    desc = models.CharField(max_length=1000, null=None, blank=True)
    uploaded_by = models.CharField(max_length=100, null=True, blank=True)
    user_id = models.CharField(max_length=100, null=True, blank=True)
    pdf = models.FileField(upload_to='pdfs/')
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)

    class Meta:
        ordering = ['titlee']

    def __str__(self):
        return f"{self.titlee}"
