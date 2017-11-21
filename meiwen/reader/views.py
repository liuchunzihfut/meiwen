from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User

from reader.models import Reader, ReaderAdditional
import datetime


def index(request):
    return HttpResponse("Hello, world. You're at the reader index.")

def fill_in_personal_information(request):
    user = request.user
    nickname = request.POST.get('nickname', '')
    name = request.POST.get('name', '')
    gender = request.POST.get('gender', '')
    birthday = request.POST.get('birthday', '')
    if not birthday:
        birthday = datetime.date.today()
    user_id = User.objects.get(username=user.username).id
    reader = Reader.objects.filter(reader_id=user_id, is_delete=False).all()
    reader.update(
        nickname = nickname,
        name = name,
        gender = gender,
        birthday = birthday
    )
    return JsonResponse({'status':200, 'message':'success'})
