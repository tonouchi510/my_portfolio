from django.http import Http404
from django.views import generic
from .models import Portfolio


class IndexView(generic.ListView):
    model = Portfolio
    template_name = 'index/index.html'
    context_object_name = 'artifacts_list'
    paginate_by = 4


def ComingSoon(request):
    raise Http404("Comming Soon...")
