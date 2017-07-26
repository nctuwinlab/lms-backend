from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return render(request, 'login.html', {'msg': 'Login Success'})
            #return HttpResponseRedirect('/')
        else:
            return render(request, 'login.html', {'msg': 'Login Failed'})
    return render(request, 'login.html')

