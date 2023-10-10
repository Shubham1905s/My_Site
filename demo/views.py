from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable': " this is sent"
    }
    return render(request,'index.html',context)
    #  return HttpResponse("This is a home page")

def home(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

    # return HttpResponse("This is a About page")


def services(request):
    return render(request,'services.html')

    # return HttpResponse("This is a services page")


def contact(request):
    return render(request,'contact.html')
