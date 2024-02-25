from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth  import authenticate,login,logout
from django.contrib import messages

def register(request):
    form = UserForm() #burada ne yaptık?
    if request.method == 'POST':
            form = UserForm(request.POST)  #burada ne yaptık?
            if form.is_valid():
                  form.save()
                  messages.success(request,'başarılı şekilde kayıt oldunuz.giriş yapabilirsiniz.')
                  return redirect('login')
    context = {
        'form':form
    }
    return render(request,'register.html',context)


def userLogin(request):
    if request.method == 'POST':
            kullanici = request.POST.get('kullanici_form')
            sifre = request.POST.get('sifre_form')

            user = authenticate(request,username = kullanici, password = sifre) #burası formdan gelen username ve password ile mi eşleştiriyor?

            if user is not None:
                  login(request,user)  
                  messages.success(request,'giriş yaptınız')
                  return redirect('index')
            else:
                  messages.error(request,'kullanıcı adı veya şifre hatalı')
    return render(request,'login.html')



def userLogout(request):
      logout(request) #burada ne yaptık?
      messages.success(request,'Çıkış Yapıldı.')
      return redirect('index')
# Create your views here.
