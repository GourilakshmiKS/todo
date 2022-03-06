from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate,login,logout

from .forms import *
from .models import *

# Create your views here.
class LoginView(View):
    def get(self,request):
        user=request.user
        if user.is_authenticated:
            return redirect('index')
        else:
            msg=""
            return render(request,'login.html',{'msg':msg})  

    def post(self,request):
        username=request.POST['username'] 
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            msg="Invalid User"
            return render(request,'login.html',{'msg':msg})              

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login')            

class Index(View):
    def get(self,request):
        user=request.user
        contact=List.objects.filter(user=user)
        context={'contact':contact}
        return render(request,'index.html',context)

class AddList(View):
    def get(self,request):
        form=AddListForm()
        context={'form':form}
        return render(request,'add.html',context)

    def post(self,request):
        user=request.user
        form=AddListForm(request.POST)            
        if form.is_valid():
            f=form.save(commit=False)
            f.user=user
            f.save()
        return redirect('index')


class EditList(View):
    def get(self,request,id):
        contact=List.objects.get(id=id)

        form=AddListForm(instance=contact)
        context={'contact':contact,'form':form}
        return render(request,'edit.html',context)

    def post(self,request,id):
        
        contact=List.objects.get(id=id)
        form=AddListForm(request.POST,instance=contact)
                    
        if form.is_valid():
            form.save()
        return redirect('index')


class DeleteList(View):
    def get(self,request,id):
        contact=List.objects.get(id=id)
        context={'contact':contact}
        return render(request,'delete.html',context)

    def post(self,request,id):
        
        contact=List.objects.get(id=id)
        contact.delete()
        return redirect('index') 
