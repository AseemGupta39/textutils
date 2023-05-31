# i have created this website
from django.http import HttpResponse



def index(request):
    return HttpResponse("<h1><pre>                                                Jai Shree Man Narayan</pre></h1>")

def about(request):
    return HttpResponse("<h1><pre>                                                Jai Shree Pashuram Bhagwan</pre></h1>")

