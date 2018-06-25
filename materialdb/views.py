from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import userdb

# Create your views here.
class tableView(ListView):
    template_name = 'tables.html'

    def get_queryset(self):
        return userdb.objects.all()


class adduserView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'user.html')

class dashboardView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'dashboard.html')
