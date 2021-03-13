from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable': 'this is sent'
    }
    return render(request, 'index.htm')
    # return HttpResponse('This is homepage')

def about(request):
    return render(request, 'about.htm')
    # return HttpResponse('This is about page')

def services(request):
    return render(request, 'services.htm')
    # return HttpResponse('This is services page')

def contact(request):
    return render(request, 'contact.htm')
    # return HttpResponse('This is contact page')