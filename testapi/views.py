import os
from django.conf import settings
from .models import UserDB
import json
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def userlist(request):
    all_users = UserDB.objects.values('auto_increment_id','name')
    print all_users
    response_data = {}
    res_data = []
    for obj in all_users:
        dummy = {}
        dummy["User ID"] = obj['auto_increment_id']
        dummy["User Name"] = obj['name']
        res_data.append(dummy)

    response_data['User List is '] = res_data
    return JsonResponse(response_data)
	
def userdetails(request,user_id):
    user_details = UserDB.objects.filter(auto_increment_id = user_id).values('auto_increment_id','name','phone','city','gender','about_me')
    response_data = {}
    res_data = []
    for obj in user_details:
        dummy = {}
        dummy["User ID"] = obj['auto_increment_id']
        dummy["User Name"] = obj['name']
        dummy["Phone Number"] = obj["phone"]
        dummy["User City"] = obj["city"]
        dummy["User Gender"] = obj["gender"]
        dummy["About Me"] = obj["about_me"]
        res_data.append(dummy)

    response_data['status'] = "200",
    response_data['User Details'] = res_data
    return JsonResponse(response_data)

@csrf_exempt
def usercreate(request):
    if request.method == "POST":
        name = request.POST.get('Name')
        phone = request.POST.get('phone', '')
        city = request.POST.get('city', '')
        gender = request.POST.get('gender')
        about_me = request.POST.get('about_me')
                
        user_create = User.objects.create(name = name, phone = phone, city = city, gender = gender, about_me = about_me)
        user_create.save()

        return JsonResponse({"status": 'User Created'})
    else:
        return JsonResponse({"Status": "Unsucessful"})

@csrf_exempt
def userdelete(request,user_id):
    if request.method == "DELETE":
    	user_obj = get_object_or_404(User, id=user_id)   
    	user_obj.delete()
    	return JsonResponse({'Status': "User deleted Sucessfully"})



