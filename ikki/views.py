from django.shortcuts import render

# Create your views here.


def yuq(request):
    return render(request, 'index.html')