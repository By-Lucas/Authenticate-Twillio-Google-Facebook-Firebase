from django.contrib.auth.password_validation import password_changed
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages import constants
from django.contrib import messages
from authentication.forms import CodeForm
from users.models import CustomUser
from .utills import send_sms

#@login_required
def home_view(request):
    return render(request, 'index.html')

def auth_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['pk'] = user.pk
            return redirect('verify-view')
    return render(request, 'auth.html',{'form':form})

def verify_view(request):
    form = CodeForm(request.POST or None)
    pk = request.session.get('pk')
    if pk:
        user = CustomUser.objects.get(pk=pk)
        code = user.code
        code_user = f"{user.username}: {user.code}"
        if not request.POST:
            # send sms
            print(code_user)
            phone_number = user.phone_number
            send_sms(code_user, user.phone_number)
        if form.is_valid():
            num = form.cleaned_data.get('number')
            if str(code) == num:
                code.save()
                login(request, user)
                messages.add_message(request, constants.SUCCESS, 'Login efetuado com sucesso!')
                return redirect('home-view')
            else:
                return redirect('login-view')

    return render(request, 'verify.html', {'form':form})

def logount_view(request):
    logout(request)
    return redirect('/')