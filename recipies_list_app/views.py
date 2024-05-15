from django.shortcuts import render
from .models import *
from recipies_project.settings import BASE_DIR
# Create your views here.

def index(request):
    # cars_data.objects.all().delete() #To Delete the data
    recipies = recipies_data.objects.all()
    return render(request, 'index.html', {'recipies':recipies, 'BASE_DIR':BASE_DIR})


def admin1(request):
    if request.method == 'POST':
        recipie = recipies_data()
        recipie.recipie_name = request.POST.get('recipie_name',False)
        recipie.recipie_description = request.POST.get('recipie_description',False)
        recipie.recipie_duration = request.POST.get('recipie_duration',False)
        recipie.recipie_ingredients = request.POST.get('recipie_ingredients',False)
        recipie.recipie_steps = request.POST.get('recipie_steps',False)
        recipie.recipie_photo = request.FILES.get("recipie_photo", False)
        recipie.save()

    
    return render(request, 'upload.html')

def add_comment(request):
    if request.method == 'POST':
        comments = comments()
        comments.comment = request.POST.get('comment',False)
        comments.username = request.POST.get('username',False)
        comments.rating = request.POST.get('ratings',False)
        comments.save()

