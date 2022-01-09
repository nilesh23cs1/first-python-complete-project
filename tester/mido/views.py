from django.shortcuts import render

def didi(request):
    content = {'fruit': 'honey'  }
    return render(request,'hi.html', content)

def about(request):
    content = { 'fruit': 'apple'}
    return render(request,'about.html', content)

def contact(request):
    content = {'fruit': 'carrot' }
    return render(request,'contact.html', content)

