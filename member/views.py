from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/member/')

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect('/member/')
        else:
            return render(request, 'login.html', {'msg': 'Login Failed'})

    return render(request, 'login.html')


@login_required
def member_home(request):
    return HttpResponse('Youre Login')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/member/login/')
