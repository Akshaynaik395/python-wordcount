from django.http import HttpResponse
from django.shortcuts import render
def home (request):
    if request.method == "POST":
        n1 = int(request.POST.get('t1'))
        n2 = int(request.POST.get('t2'))
        btn = request.POST.get("btn")
        if btn == "add":
            n3 = n1 + n2
            return render(request, 'home.html', {'result': n3,'n1':n1,'n2':n2})
        elif btn == "sub":
            n3 = n1 - n2
            return render(request, 'home.html', {'result': n3,'n1':n1,'n2':n2})
        elif btn == "mul":
            n3 = n1 * n2
            return render(request, 'home.html', {'result': n3,'n1':n1,'n2':n2})
        elif btn == "div":
            n3 = n1 / n2
            return render(request, 'home.html', {'result': n3,'n1':n1,'n2':n2})
    else:
        return render(request, 'home.html', {'name':"akshay"})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def cal(request):
    print()

    # n1 = int(request.POST.get('t1'))
    # n2 = int(request.POST.get('t2'))
    # btn=request.POST.get("btn")
    # if btn=="add":
    #     n3=n1+n2
    #     return render(request,'cal.html',{'result':n3})
    # elif btn=="sub":
    #     n3=n1-n2
    #     return render(request,'cal.html',{'result':n3})
    # elif btn=="mul":
    #     n3=n1*n2
    #     return render(request,'cal.html',{'result':n3})
    # elif btn=="div":
    #     n3=n1/n2
    #     return render(request,'cal.html',{'result':n3})
def word(request):
    return render(request, 'word.html')

def count(request):
    val1 =request.GET.get('chk1','off')
    val2 = request.GET.get('chk2', 'off')
    val3 = request.GET.get('chk3', 'off')
    val4 = request.GET.get('chk4', 'off')
    val5 = request.GET.get('chk5', 'off')
    data = request.GET.get('txt')

    if val1 =='on':
        params={"purpose":"information","result":data}
        return render(request,'count.html',params)
    elif val2 =='on':
        word_list =data.split()
        word_len =len(word_list)
        params = {"purpose": "word count", "result": word_len}
        return render(request, 'count.html', params)
    elif val4 =='on':
        occurance=data.upper()
        params = {"purpose": "upper case", "result": occurance}
        return render(request, 'count.html', params)



    return render(request, 'count.html',{'info':data})
