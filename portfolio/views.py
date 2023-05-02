from django.shortcuts import render

# Create your views here.


def home(request):
    context = {
        'sidebar': 'home',
        }
    return render(request, 'portfolio/index.html', context)

def about(request):
    context = {
        'sidebar': 'about',
        }
    return render (request,'portfolio/about.html',context )

def portfolio(request):
    context = {
        'sidebar': 'portfolio',
        }
    return render (request,'portfolio/portfolio.html',context )

def contact(request):
    context = {
        'sidebar': 'contact',
        }
    return render (request,'portfolio/contact.html',context )