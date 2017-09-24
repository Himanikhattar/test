import os
from .models import UserDB
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse


def userlist(request):
    all_users = UserDB.objects.values('auto_increment_id','name')
    response_data = {}
    res_data = []
    for obj in all_users:
        dummy = {}
        dummy["User ID"] = obj['auto_increment_id']
        dummy["User Name"] = obj['name']
        res_data.append(dummy)

    response_data['User List is '] = res_data
    return JsonResponse(response_data)

@csrf_exempt	
def userdetails(request,user_id):

    if request.method == "DELETE":
        user_obj = get_object_or_404(UserDB, auto_increment_id = user_id)   
        user_obj.delete()
        return JsonResponse({'Status': "User deleted Sucessfully"})

    else :
        user_details = UserDB.objects.filter(auto_increment_id = user_id).values('auto_increment_id','name','phone','city',\
        'gender','about_me')
        image = {}
        tempimage = []
        for obj in user_details:
            dummy = {}
            dummy["User ID"] = obj['auto_increment_id']
            dummy["User Name"] = obj['name']
            dummy["Phone Number"] = obj["phone"]
            dummy["User City"] = obj["city"]
            dummy["User Gender"] = obj["gender"]
            dummy["About Me"] = obj["about_me"]
            tempimage.append(dummy)

        image['status'] = "200",
        image['User Details'] = tempimage
        return JsonResponse(image)

@csrf_exempt
def user_create(request):
    if request.method == "POST":
        name = request.POST.get('Name')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        gender = request.POST.get('gender')
                
        user_create = UserDB.objects.create(name = name,phone = phone,city = city,gender = gender)  
        user_create.save()

        return JsonResponse({"status": 'User Created'})
    else:
        return JsonResponse({"Status": "Unsucessful"})
