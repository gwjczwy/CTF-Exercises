from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


def index(requests):
    return render(requests,'tools/index.html',{'toolname':'index'})

def shop(requests):
    data={}
    data['toolName']="shop"
    return render(requests, 'tools/index.html', data)

def surl(requests):
    data={}
    data['toolName']="surl"
    data['parameter']="index"
    return render(requests, 'tools/index.html', data)

def surls(requests,parameter):
    data={}
    data['toolName']="surl"
    data['parameter']="link"
    print(parameter)


    return render(requests, 'tools/index.html', data)

    
def surls(requests,parameter):
    data={}
    data['toolName']="logs"
    print(parameter)


    return render(requests, 'tools/index.html', data)