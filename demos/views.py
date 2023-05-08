from django.shortcuts import render
from django.http import HttpResponse
from API_SYSTEM.weather_finding import show
from django.shortcuts import render, redirect
from API_SYSTEM.open_chat_api import api_answer
# Create your views here.



def result(request,a):
    gender = request.GET.get('gender')
    category = request.GET.get('category')
    b = show()
    c= b + '저는' + str(gender) +'이고' + str(b) + '오늘은' + str(category)+ '스타일로 입고 싶네요'
    d = api_answer(c)
    context = {
        'category' : category,
        'gender' : gender,
        'question' : c,
        'answer' :d,
    }
    

    return render(request, 'result.html', context)


def choose(request):
    b = show()
    context ={
        'b' : b,
    }
    return render(request, 'choose.html',context)

