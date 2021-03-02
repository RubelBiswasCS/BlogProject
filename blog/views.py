from django.shortcuts import render
from django.http import HttpResponse

posts =[
    {
    'author':'Jay',
    'title':'Blog Post 1',
    'content':'content of first post',
    'date':'June 12, 2020'
    },

    {
    'author':'Kay',
    'title':'Blog Post 2',
    'content':'content of second post',
    'date' : 'January 10, 2021'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})   

