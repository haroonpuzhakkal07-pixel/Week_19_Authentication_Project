from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home_view(request):
    if request.user.is_superuser:
        return HttpResponse("Welcome Admin")
    elif request.user.is_superuser:
        return HttpResponse("Welcome Staff")
    else:
        return HttpResponse(f"Welcome User({request.user.username})")

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def admin_only_view(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not allowed here")
    return HttpResponse("Welcome Admin Panel")

@login_required
def special_view(request):
    if request.user.has_perm('auth.view_user'):
        return HttpResponse("You can view users")
    return HttpResponse("Permission Denied")