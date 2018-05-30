from django.views import generic
from .models import MNIST
from django.shortcuts import render


# Create your views here.
class MainView(generic.ListView):
    model = MNIST
    template_name = 'mnist/mnist.html'
    context_object_name = 'digit_list'


def detail(request):
    return render(request, 'mnist/detail.html', {})
