from django.db import models

CHOICE = (
            (0, '0'),
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9')
        )


class MNIST(models.Model):
    data_id = models.IntegerField(default=1, primary_key=True)
    path = models.CharField(max_length=50)
    label = models.IntegerField(choices=CHOICE)

    def __str__(self):
        return str(self.label)

    def is_label_valid_values(self):
        return self.label >= 0 or self.label < 10

    def getId(self):
        return self.id

    def predict(self, path):
        return path



