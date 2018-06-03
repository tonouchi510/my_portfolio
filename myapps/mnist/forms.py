from django.forms import ModelForm
from .models import MNIST


class MNISTForm(ModelForm):
    class Meta:
        model = MNIST
        fields = ['data_id', 'path', 'label']



