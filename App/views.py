from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
# Create your views here.

class UserTest(View):
    def get(self,request):
        return JsonResponse({'method':'GET'})

    def post(self,request):
        return JsonResponse({'method':'POST'})

    def put(self,requset):
        return JsonResponse({'method':'PUT'})

    def delete(self,request):
        return JsonResponse({'method':'delete'})





