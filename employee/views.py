from django.shortcuts import render, redirect
from django.views import View
from employee.forms import EmployeeForm, RegistrationForm, LoginForm
from employee.models import Employees
from django.views.generic import TemplateView, CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout


class IndexView(TemplateView):
    template_name = 'index.html'


class SignupView(CreateView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('signin')


class SigninView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')
            user = authenticate(request, username=uname, password=pwd)
            if user:
                login(request, user)
                return redirect('home')
            else:
                return render(request, self.template_name, {'form': form})


class EmployeeCreateView(View):

    def get(self, request, *args, **kw):
        form = EmployeeForm()
        return render(request, 'add-employee.html', {'form': form})

    def post(self, request, *args, **kw):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add-employee')
        else:
            return render(request, 'add-employee.html', {'form': form})


class EmployeeListView(View):

    def get(self, request, *args, **kw):
        qs = Employees.objects.all()
        return render(request, 'list-employee.html', {'todo': qs})


class EmployeeDetail(View):

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        qs = Employees.objects.get(id=id)
        return render(request, 'detail-employee.html', {'detail': qs})


class EmployeeDelete(View):

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        Employees.objects.get(id=id).delete()
        return redirect('list-employee')
