from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import userdb

# Create your views here.
class tableView(ListView):
    template_name = 'tables.html'

    def get_queryset(self):
        return userdb.objects.all()


class adduserView(TemplateView):
    template_name = 'adduser.html'

    def get_queryset(self):
        return userdb.objects.all()

class dashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_queryset(self):
        return userdb.objects.all()
