from django.views import generic
from .models import MNIST


# Create your views here.
class MainView(generic.ListView):
    model = MNIST
    template_name = 'mnist/mnist.html'
    context_object_name = 'digit_list'

