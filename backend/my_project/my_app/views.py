# tasks/views.py
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.authtoken.models import Token  # Import Token model
from rest_framework.decorators import authentication_classes, permission_classes ,api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.decorators import login_required

from .models import Community

from .serializer import CommunitySerializer  # convert queryset to json

# register


@csrf_exempt
def user_register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data['email']
        username = data['username']
        password = data['password']
        User.objects.create_user(
            email=email, username=username, password=password)
        return JsonResponse({'message': 'User registered successfully'})

# login


@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Generate or retrieve an existing token for the user
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({'message': 'Login successful', 'token': token.key , "username":username})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)


# Logout Route
@csrf_exempt
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'Logout successful'})

# protected route


@csrf_exempt
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@login_required
def data(request):
    if request.method == 'GET':

        return JsonResponse({'message': 'Protected data accessed successfully'})
    else:
        return JsonResponse({"msg": "please login first"})


# Get a list of all communities
@csrf_exempt
def list_communities(request):
    if request.method == 'GET':
        communities = Community.objects.all()
        serializer = CommunitySerializer(communities, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)


# Create a new community
# @csrf_exempt
# @api_view(['POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
@csrf_exempt
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
# @login_required
def create_community(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        description = data.get('description')
        community = Community(description=description)
        community.save()
        return JsonResponse({'message': 'Community created successfully'}, status=201)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)
    

