from django.db import models


class Portfolio(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published', null=True, blank=True)
    path = models.CharField(max_length=50, null=True, blank=True)
    image = models.CharField(max_length=50)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.title
