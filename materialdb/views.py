from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.template import RequestContext
from .models import Person
from materialdb.forms import AddPerson


class dashboardView(ListView):
    template_name = 'dashboard.html'

    def get_queryset(self):
        return Person.objects.all()

class tableView(ListView):
    template_name = 'tables.html'

    def get_queryset(self):
        return Person.objects.all()

    def post(self, request):
        form = AddPerson(request.POST or None)

        context = { 'form': form }
        if 'deleteEntry' in request.POST:
            id_num = request.POST['deleteEntry']
            Person.objects.filter(id=id_num).delete()

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

class addpersonView(TemplateView):
    template_name = 'addperson.html'

    def get(self, request):
        form = AddPerson()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = AddPerson(request.POST or None)

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


            Person.objects.create_user(first_name, last_name, country, city, salary)
            return redirect('/')

        return render(request, self.template_name, context)

class editpersonView(TemplateView):
    template_name = 'editperson.html'

    def get(self, request):
        form = AddPerson()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = AddPerson(request.POST or None)
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

            person = Person.objects.filter(id=id_num).update(first_name=first_name, last_name=last_name, salary=salary, country=country,city=city)

            return redirect('/')
        return render(request, self.template_name, context)