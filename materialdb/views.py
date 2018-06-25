from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import userdb
from materialdb.forms import AddUser
import pymysql

# Create your views here.

class dashboardView(ListView):
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

            conn = pymysql.connect(host="192.168.1.12", port=3306, user="root", password="admin123", db="userdb")

            mysql = conn.cursor()

            sql_lookup = "select * from userdb.materialdb_userdb;"


            sql_add = ("insert into userdb.materialdb_userdb (first_name,last_name, country,city,salary ) values ('%s','%s', '%s', '%s', '%s');" % (first_name, last_name, country, city, salary))
            sql_commit = "SET autocommit = 1;"

            mysql.execute(sql_add)
            mysql.execute(sql_commit)

        return render(request, self.template_name, context)
