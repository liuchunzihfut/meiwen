from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Hello, world. You're at the writer index.")

def applyWrite(request):
    user = request.user
    user_id = user.id
    data = request.POST.get()
    return JsonResponse()
