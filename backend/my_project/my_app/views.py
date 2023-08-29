from django.shortcuts import render,redirect
import json
from django.http import Http404, JsonResponse
from my_app.models import register
from django.views.decorators.csrf import csrf_exempt

#default route
def default_path(request):
    return render(request, 'home.html')


# view menu
def register_users(request):
    # menu_items = register.objects.all()  # Retrieve all dishes from the database
    return JsonResponse({'menu': "tarun"})



@csrf_exempt
def register_post(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        # if not name or not email or not password:
        #     return JsonResponse({'error': 'Missing required fields'}, status=400)

        user = register(name=name, email=email, password=password)
        user.save();
        
        return JsonResponse({"msg": "User registered successfully"})
    else:
        return JsonResponse({'msg': 'Wrong request made'}, status=400)
