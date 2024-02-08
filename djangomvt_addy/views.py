from django.shortcuts import render
def home(request):
    return render(request,'home.html')
def fun(request):
    return render(request,'myproject.html')
def fun2(request):
    a=request.GET['user_input']
    a=a.upper()
    return render(request,'myproject_FormResult.html',{'form_input':a})

    
