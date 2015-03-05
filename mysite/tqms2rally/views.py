from django.shortcuts import render
from django.views import generic
from tqms2rally.models import viewNavigation
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'upload/index.html'
    def get_queryset(self):
        return viewNavigation.object.order_by('')[:5]
        return Question.objects.order_by('-pub_date')[:5]