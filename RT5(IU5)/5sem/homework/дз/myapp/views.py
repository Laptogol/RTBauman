from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView, FormView
from myapp.models import *
from myapp.forms import *
from django.contrib.auth.forms import UserCreationForm

# Опять же, спасибо django за готовую форму аутентификации.
from django.contrib.auth.forms import AuthenticationForm

# Функция для установки сессионного ключа.
# По нему django будет определять, выполнил ли вход пользователь.
from django.contrib.auth import login
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout


class UserList2(ListView):
    model = User2
    template_name = "user2_list.html"
    context_object_name = "obj_list"

    def get(self, request, *args, **kwargs):
        self.id = request.GET.get('id')
        return super(UserList2, self).get(request, *args, **kwargs)


def concerts(request, course_id=6):
    if request.method == 'POST':
        Concert.objects.get(id_course=course_id).course_users.add(request.user)
    return render(request, "concert.html", {'concerts': Concert.objects.get(id_course=course_id)}, locals())


def concerts_add(request):
    if request.method == "POST":
        form = CoForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.name = request.POST.get('name')
            post.save()
            return HttpResponseRedirect("/")
    else:
        form = CoForm()
    return render(request, 'newedit.html', {'form': form})


def user_add(request):
        Users = User2.objects.all()
        Concerts = Concert.objects.all()
        form = UsForm(request.POST)
        context = {"form": form, "Users": Users, "Concerts": Concerts}
        if form.is_valid():
            post = form.save()
            post.name = request.POST.get('name')
            post.idconcert = request.POST.get('Concert')
            post.save()
            return HttpResponseRedirect("/")
        return render(request, 'addpost.html', context)


class LogoutView(View):
    def get(self, request):

        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/login/")


class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)