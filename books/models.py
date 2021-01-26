from django.db import models

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    realease_year = models.IntegerField()
    state = models.CharField(max_length=50)
    pages = models.IntegerField()
    publisher_company = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
