from django.shortcuts import render
# from django.http import HttpResponse


def MainPage_index(request):
    return render(request, 'MainPage/MainPage.html', {})

