from django.shortcuts import render


def home(request):
    return render(request, "exemple/home.html")
