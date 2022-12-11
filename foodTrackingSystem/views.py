from django.shortcuts import render

def insert_code(request):
    return render(request, 'foodTrackingSystem/insert_code.html')
