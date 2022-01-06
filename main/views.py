from django.http import JsonResponse
from rest_framework import status, permissions
from rest_framework_simplejwt import authentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import *



@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def index(request):
    # displaying home page with list of users for admin only
    group = request.user.groups.all()[0].name
    if group == 'Admin':
        users = User.objects.all()

        data = list(users.values(
            "username", "first_name", "email", "date_joined"))
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({"data": "only admins can view list of users"})


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def userpage(request):
    # displaying user page with sub users for that user
    subusers = SubUsers.objects.filter(owner=request.user)
    data = list(subusers.values("name", "phone", "email", "date_created"))
    return JsonResponse(data, safe=False)


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def createsubuser(request):
    # creating a subuser associated with a user
    #Getting posted data
    data = request.data
    try:
        #getting fields
        owner = request.user
        name = data["name"]
        phone = data["phone"]
        email = data["email"]
        #Saving data to database
        s= SubUsers(owner=owner, name=name, phone=phone, email=email)
        s.save()
        return JsonResponse({"success": "Sub user creating successfully"})
    except:
        return JsonResponse({"Error": "Something went wrong"})
