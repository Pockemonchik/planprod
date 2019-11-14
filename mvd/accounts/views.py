from django.shortcuts import render,reverse,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout


# Create your views here.
def log(request):
    form=AuthenticationForm(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return render(request, 'login.html',{'form': form})
    else:
        form=AuthenticationForm()
        return render(request, 'login.html',{'form': form})


def logout_view(request):
    logout(request)
    return redirect('log')
