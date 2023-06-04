# i have created this website
from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     return HttpResponse("<h1><pre>                                                Jai Shree Man Narayan</pre></h1>")

# def about(request):
#     return HttpResponse("<h1><pre>                                                Jai Shree Pashuram Bhagwan</pre></h1>")

def index(request):
    # params = {'name':'aseem','place':'harry'}
    return render(request,'index.html')
    # return HttpResponse("<h1>Home </h1>")

def analyze(request):
    dj_text = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    print(dj_text)
    print(removepunc)
    # analysed = dj_text
    punctuations = """!(){}[]":;'?/.>,<-+=|\@#$%^&*~`"""
    analysed = ""
    for char in dj_text:
        if char not in punctuations:
            analysed = analysed + char
            
    params = {'purpose':'removed  punctua','analysed_text':analysed}
    return render(request,'analyze.html',params)
    # return HttpResponse("<h1>remove punc </h1>")    


# def removepunc(request):
#     dj_text = request.GET.get('text','default')
#     print(dj_text)
#     return HttpResponse("<h1>remove punc</h1>")

# def capfirst(request):
#     return HttpResponse("<h1>capitalize first</h1>")

# def newlineremove(request):
#     return HttpResponse("<h1>nlr</h1>")

# def spaceremove(request):
#     return HttpResponse("<h1>space rem</h1>")

# def charcount(request):
#     return HttpResponse("<h1>char count</h1>")
