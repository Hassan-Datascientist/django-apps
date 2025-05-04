from django.shortcuts import render
from django.http import HttpResponse
from .models import calculation



# Create your views here.

def greet(request):
    result = 0
    if request.method =='POST':
        number1 = int( request.POST.get('number1'))
        number2 = int(request.POST.get('number2'))
        
        result = number1+number2
        calculation.objects.create(number1 = number1 , number2= number2)
        
        
    
        
    return render(request, 'sum.html',{"result":result})
        

   # return HttpResponse("Hello word!")
   
