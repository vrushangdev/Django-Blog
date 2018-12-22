from django.shortcuts import render
from django.http import HttpResponse

posts =[
    {
        'author':'Vrushang Desai',
        'title':'Blog Post One',
        'content':'First Post Content',
        'date_posted':'August 27, 2018'
    },
     {
        'author':'Bull Desai',
        'title':'Blog Post two',
        'content':'Second Post Content',
        'date_posted':'August 28, 2018'
    }
]


def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)
def about(request):
    return render(request,'blog/about.html',{'title':'About'})    