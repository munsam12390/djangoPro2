from django.shortcuts import render
from application1.models import employees
from django.http import HttpResponse
def test_case1(request):
    try:
        obj = employees.objects.all()
        print(obj)
        
    except:
        return HttpResponse("try block has error so i get executed")
    else:
        return HttpResponse("There is no error in try block so i executed")
    finally:
        return HttpResponse("Wheather there is error or not i will be executed")
    return HttpResponse(obj)
   



# Create your views here.
