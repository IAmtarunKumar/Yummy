# tasks/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User, Recipe


@csrf_exempt
def task_list(request):
    if request.method == 'GET':

        tasks = User.objects.all()
        task_list = [{'name': task.name, 'email': task.email,
                      'password': task.password} for task in tasks]
        return JsonResponse(task_list, safe=False)


@csrf_exempt
def userRegister(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        task = User(name=data['name'], email=data['email'],
                    password=data['password'])
        task.save()
        return JsonResponse({'message': 'User register successfully'})


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        # Extract the task name from the request data
        password = data.get('password')

        try:
            task = User.objects.get(email=email, password=password)
            return JsonResponse({'message': 'Login successful'})
        except User.DoesNotExist:
            return JsonResponse({'message': 'Please Login First'}, status=401)


# Recipes api

@csrf_exempt
def showRecipe(request):
    if request.method == 'GET':

        tasks = Recipe.objects.all()
        recipe_list = [{'user_id' : recipes.user_id ,  'title': recipes.title, 'ingredients': recipes.ingredients,
                        'instructions': recipes.instructions} for recipes in tasks]
        return JsonResponse(recipe_list, safe=False)

# Add recipe


@csrf_exempt
def addRecipe(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        recipe = Recipe( user_id=data['user_id'], title=data['title'], ingredients=data['ingredients'], instructions=data['instructions'])
        recipe.save()
        return JsonResponse({'message': 'Recipe Post successfully'})

# @csrf_exempt
# def task_list(request):
#     if request.method == 'GET':
#         tasks = User.objects.all()
#         task_list = [{'id': task.id, 'name': task.name, 'completed': task.completed} for task in tasks]
#         return JsonResponse(task_list, safe=False)
#     elif request.method == 'POST':
#         data = json.loads(request.body)
#         task = User(name=data['name'], completed=data['completed'])
#         task.save()
#         return JsonResponse({'message': 'Task created successfully'})

# @csrf_exempt
# def task_detail(request, user_id):
#     try:
#         task = User.objects.get(pk=user_id)
#     except User.DoesNotExist:
#         return JsonResponse({'message': 'Task not found'}, status=404)

#     if request.method == 'GET':
#         task_data = {'id': task.id, 'name': task.name, 'completed': task.completed}
#         return JsonResponse(task_data)
#     elif request.method == 'PUT':
#         data = json.loads(request.body)
#         task.name = data['name']
#         task.completed = data['completed']
#         task.save()
#         return JsonResponse({'message': 'Task updated successfully'})
#     elif request.method == 'DELETE':
#         task.delete()
#         return JsonResponse({'message': 'Task deleted successfully'})

# @csrf_exempt
# def login(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         email = data.get('email')
#         password = data.get('password')  # Extract the task name from the request data


#         try:
#             task = User.objects.get(email=email , password=password)
#             return JsonResponse({'message': 'Login successful'})
#         except User.DoesNotExist:
#             return JsonResponse({'message': 'Please Login First'}, status=401)
