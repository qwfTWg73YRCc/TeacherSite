from django.shortcuts import render
# from django.http import HttpResponse


def MainPage(request):
    return render(request, 'MainPage/MainPage.html', {})

def About(request):
    return render(request, 'MainPage/About.html', {})


