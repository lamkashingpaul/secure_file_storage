from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from codes.forms import CodeForm
from members.models import MyCloudUser
from .forms import RegisterUserForm
from .utils import send_sms


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['pk'] = user.pk
            return redirect('verify')
        else:
            messages.success(request, 'Error logging in')
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})


def verify_user(request):
    form = CodeForm(request.POST or None)
    pk = request.session.get('pk')
    user_query = MyCloudUser.objects.filter(pk=pk)

    if pk and user_query:
        user = user_query.first()
        code = user.code
        code_user = f'{user.username}: {code}'
        if not request.POST:
            # send code to user
            print(code_user)
            send_sms(code_user, user.phone_number)

        if form.is_valid():
            num = form.cleaned_data.get('number')

            if str(code) == num:
                code.save()
                login(request, user)
                messages.success(request, 'You have successfully logged in')
                return redirect('home')
            else:
                messages.success(request, 'Error logging in')
                return redirect('login')

    return render(request, 'authenticate/verify_user.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have logged out')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Registration Successful!'))
            return redirect('home')
    else:
        form = RegisterUserForm()

    return render(request, 'authenticate/register_user.html', {'form': form})
