from django.shortcuts import render, redirect
from datetime import datetime
from home.models import *
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def chocolate(request):
    return render(request, "chocolate.html")


def dry_fruit(request):
    return render(request, "dry_fruit.html")


def choco_chip(request):
    return render(request, "choco_chip.html")


def family_icecream(request):
    return render(request, "family_icecream.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())
        contact.save()
        messages.success(
            request, "Your franchie form submit successfully!! Thank you")
        
        return redirect('/contact/')

    return render(request, "contact.html")


def feedback(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        feedback = Feedback(name=name, email=email, phone=phone, desc=desc)
        feedback.save()
        messages.success(
            request, "Your feedback form submit successfully!! Thanks for your feedback")

        return redirect('/contact/')

    return render(request, "contact.html")

def ice_recipes(request):
    if request.method == "POST":
        data = request.POST
        ice_image = request.FILES.get('ice_image')
        ice_name = data.get('ice_name')
        ice_discription = data.get('ice_discription')

        Ice_recipe.objects.create(
            ice_image = ice_image,
            ice_name = ice_name,
            ice_discription = ice_discription,
        )
        return redirect('/ice_recipes')
    
    queryset = Ice_recipe.objects.all()
    context = {'ice_recipes' : queryset}
    
    return render(request, "ice_recipes.html", context)

def update_recipe(request, id):
    queryset = Ice_recipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        ice_image = request.FILES.get('ice_image')
        ice_name = data.get('ice_name')
        ice_discription = data.get('ice_discription')

        queryset.ice_name = ice_name
        queryset.ice_discription = ice_discription

        if ice_image:
            queryset.ice_image = ice_image
        
        queryset.save()
        return redirect('/ice_recipes')

    if request.GET.get('search'):
        queryset = queryset.filter(ice_name__icontains = request.GET.get('search'))


    context = {'recipe': queryset}

    return render(request , 'update_ice.html', context)

def delete_ice (request, id):
    queryset = Ice_recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/ice_recipes')