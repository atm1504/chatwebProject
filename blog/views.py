from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts=[
    {
        'author':'Atm',
        'title':'love',
        'content':'Amartya loves atm',
        'date_posted':'August 15, 2000'
    },
    {
        'author':'Amartys',
        'title':'lovely',
        'content':'Atm loves amartya',
        'date_posted':'January 4, 2000'
    }
]
def home(request):
    context={
        'posts':posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})    