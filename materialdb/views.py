from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import userdb
from materialdb.forms import AddUser

# Create your views here.

class dashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_queryset(self):
        return userdb.objects.all()

class tableView(ListView):
    template_name = 'tables.html'

    def get_queryset(self):
        return userdb.objects.all()


class adduserView(TemplateView):
    template_name = 'adduser.html'

    def get(self, request):
        form = AddUser()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = AddUser(request.POST or None)

        context = { 'form': form }
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            context.update({'first_name': first_name})

            last_name = form.cleaned_data['last_name']
            context.update({'last_name': last_name})

            salary = form.cleaned_data['salary']
            context.update({'salary': salary})

            country = form.cleaned_data['country']
            context.update({'country': country})

            city = form.cleaned_data['city']
            context.update({'city': city})

            id_num = form.cleaned_data['id_num']
            context.update({'id_num': id_num})

        return render(request, self.template_name, context)
