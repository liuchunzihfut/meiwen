from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from writer.models import Writer, Group
from reader.models import Reader, ReaderAdditional


def index(request):
    return HttpResponse("Hello, world. You're at the writer index.")

def applyWrite(request):
    user = request.user
    user_id = user.id
    phone_num = request.POST.get('phone_num')
    ID_number = request.POST.get('ID_number')
    reader_detail = Reader.objects.filter(reader_id=user_id).all()        
    if phone_num and ID_number and reader_detail:
        writer = Writer.objects.filter(write_id=user_id).all()
        if writer:
            writer.update(
                phone_num=phone_num,
                ID_number=ID_number,
            )
        else:
            writer = Writer(
                reader_id=user_id,
                write_id=user_id,
                phone_num=phone_num,
                ID_number=ID_number,
            )
            writer.save()
        return JsonResponse({'status': 200, 'message':'success'})
    else:
        return JsonResponse({'status': 600, 'message':'please sign up please'})
