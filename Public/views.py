from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserAddForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .decorators import Admin_only
from Product.models import ProductDetails

@Admin_only
def Index(request):
    Product = ProductDetails.objects.all()
    context ={
        "Product":Product
    }
    return render(request,'Index.html',context)

def AdminIndex(request):
    return render(request,"adminhome.html")

def SignIn(request):
    if request.method== "POST":
        username = request.POST["uname"]
        password = request.POST["pswd"]
        user = authenticate(request,username = username ,password = password)

        if user is not None:
            login(request,user)
            return redirect("Index")
        else:
            messages.info(request,"Username or password incorrect")
    return render(request,'login.html')

def SignUp(request):
    form = UserAddForm()

    if request.method == "POST":
        form=UserAddForm(request.POST)

        if form.is_valid():
            username=form.cleaned_data.get("username")
            email=form.cleaned_data.get("email")

            if User.objects.filter(username=username).exists():
                 messages.info(request,"username already Exists")
                 return redirect('SignUp')

            if User.objects.filter(email=email).exists():
                messages.info(request,"email already Exists")
                return redirect('SignUp')
            else:
                form.save()
                messages.success(request,"user created")
                return redirect('SignIn')
    context = {
        "form":form
    }
    return render(request,'register.html',context)

def SignOut(request):
    logout(request)
    return redirect('Index')

