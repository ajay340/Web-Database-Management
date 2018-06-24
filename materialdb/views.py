from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class tableView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'tables.html', context=None)

class adduserView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'user.html', context=None)

class dashboardView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'dashboard.html', context=None)
