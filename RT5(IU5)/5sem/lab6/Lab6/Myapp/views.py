from django.http import HttpResponse
from django.views.generic import View
from Myapp.Connection import *
from django.views.generic import ListView

class UserList(ListView):
    model = User

class UserList(View):
    def get(self, request, *args, **kwargs):
        con = Connection("root", "1111", "userbronkoncert")
        with con:
            user = SelAll(con)
            f=user.save()
        return HttpResponse(f)





class MyView(View):

    def get(self, request, *args, **kwargs):
        f=['Hello, World!','<br>','sdf']
        return HttpResponse(f)