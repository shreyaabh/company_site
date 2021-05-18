from django.shortcuts import render
from .models import About, ContactUs


def home(request):
    return render(request, "Home/index.html")


def about(request):
    abouts = About.objects.all()
    return render(request, "Home/about.html", {"abouts": abouts})


def services(request):
    return render(request, "Home/services.html")


def contact(request):

    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        content = request.POST["content"]
        contact = ContactUs(name=name, email=email, content=content)
        contact.save()

    return render(request, "Home/contact.html")

