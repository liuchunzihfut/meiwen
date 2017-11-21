from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from writer.models import Writer, Group, ApplyGroup
from reader.models import Reader, ReaderAdditional

import datetime


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

def creatGroup(request):
    user = request.user
    user_id = user.id
    user_write = Writer.objects.filter(writer_id=user_id)
    if user_write:
        group = Group(
            group_name = request.POST.get('group_name'),
            group_member_id = user_id,
            group_mumber_number = 1,
            group_admin_id = user_id,
        )
        group.save()
        return JsonResponse({'status':200, 'message':'success'})
    return JsonResponse({'message':'please apply write at first'}, status=601)

def applyGroup(request):
    user = request.user
    user_id = user.id
    group_id = request.POST.get('group_id')
    message = request.POST.get('message', '')
    now = datetime.datetime.now()
    apply = ApplyGroup(
        user_id=user_id,
        group_id=group_id,
        apply_type='user_apply',
        apply_status='applying',
        apply_message=message,
        create_time=now
    )
    apply.save()
    return JsonResponse({'status': 200, 'message': 'success'})

def replyApply(request):
    """
    reply_status = 1, approve
    reply_status = 2, reject
    """
    reply_map = {
        1: 'approved',
        2: 'rejected',
    }
    apply_id = request.POST.get('apply_id')
    reply_status = request.POST.get('reply_status')
    reply_status = reply_map.get(reply_status)
    now = datetime.datetime.now()
    ApplyGroup.objects.filter(id=apply_id, is_delete=False).update(apply_status=reply_status, finish_time=now)
    return JsonResponse({'status': 200, 'message': 'success'})

def myApplyShow(request):
    user = request.user
    user_id = user.id
    apply_list = ApplyGroup.objects.filter(
        user_id = user_id, is_delete=False
    ).all()
    return JsonResponse({'apply_list': apply_list})

def otherApplyShow(request):
    user_id = request.user.id
    group_admin_list = Group.objects.filter(group_admin_id=user_id).values('id')
    apply_list_unreply = ApplyGroup.objects.filter(
        group_id__in=group_admin_list, apply_status='applying', is_delete=False)
    apply_list_reply = ApplyGroup.objects.filter(
        group_id__in=group_admin_list, apply_status__in=['approved', 'rejected'], is_delete=False)
    return JsonResponse({'apply_unreply': apply_list_unreply, 'apply_reply': apply_list_reply})






