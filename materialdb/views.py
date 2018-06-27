from django.shortcuts import render, render_to_response, redirect
from django.views.generic import TemplateView, ListView
from django.template import RequestContext
from .models import userdb
from materialdb.forms import AddUser
import pymysql

conn = pymysql.connect(host="", port=, user="", password="", db="userdb")
mysql = conn.cursor()

# Create your views here.

class dashboardView(ListView):
    template_name = 'dashboard.html'

    def get_queryset(self):
        return userdb.objects.all()

class tableView(ListView):
    template_name = 'tables.html'

    def get_queryset(self):
        return userdb.objects.all()

    def post(self, request):
        form = AddUser(request.POST or None)

        context = { 'form': form }
        if 'deleteEntry' in request.POST:
            id_num = request.POST['deleteEntry']



            sql_delete = ("delete from userdb.materialdb_userdb where id ='%s';" % (id_num))
            sql_commit = "SET autocommit = 1;"
            mysql.execute(sql_delete)
            mysql.execute(sql_commit)

            return redirect('/')

        elif 'editEntry' in request.POST:

            values = request.POST['editEntry']
            values = values.split(',')
            request.session['id_num'] = values[0]
            request.session['first_name'] = values[1]
            request.session['last_name'] = values[2]
            request.session['country'] = values[3]
            request.session['city'] = values[4]
            request.session['salary'] = values[5]

            return redirect('/edit')

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



            sql_lookup = "select * from userdb.materialdb_userdb;"

            sql_add = ("insert into userdb.materialdb_userdb (first_name,last_name, country,city,salary ) values ('%s','%s', '%s', '%s', '%s');" % (first_name, last_name, country, city, salary))
            sql_commit = "SET autocommit = 1;"

            mysql.execute(sql_add)
            mysql.execute(sql_commit)

        return render(request, self.template_name, context)

class edituserView(TemplateView):
    template_name = 'edituser.html'

    def get(self, request):
        form = AddUser()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = AddUser(request.POST or None)
        context = { 'form': form }
        if form.is_valid():

            id_num = request.POST['id_num']
            context.update({'id_num': id_num})

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


            sql_update = ("update userdb.materialdb_userdb set first_name = '%s', last_name = '%s', country = '%s', city = '%s', salary = '%s' where id = '%s';" % (first_name, last_name, country, city, salary, id_num))
            sql_commit = "SET autocommit = 1;"
            mysql.execute(sql_update)
            mysql.execute(sql_commit)

            return redirect('/')
