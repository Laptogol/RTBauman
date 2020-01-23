
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View



class ExampleView(View):
    def get(self, request):
        url_name = request.GET.get('name')
        return render(request, 'example.html', {"my_variable": "Этот текстподставится вместо переменной"}),

class OrdersView(View):
    def get(self, request):
        data ={
            'name':request.GET.get('name'),
            'orders': (
                {'title': 'Первый заказ', 'id': 1},
                {'title': 'Второй заказ', 'id': 2},
                {'title': 'Третий заказ', 'id': 3}
            )
        }
        return render(request, "orders.html",data)


class OrderView(View):
    def get(self, request, id):
        data = {
            'order':{
               'id': id
            }
        }
        return render(request, 'order.html',data)