from django.db import models


# Create your models here.
class MNIST(models.Model):
    data_id = models.IntegerField(default=0, primary_key=True)
    path = models.CharField(max_length=50)
    label = models.IntegerField(default=0)

    def __str__(self):
        return str(self.label)

    def is_label_valid_values(self):
        return self.label >= 0 or self.label < 10

