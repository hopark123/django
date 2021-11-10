from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth import login, logout
from django.contrib.auth import views as auth_views

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('main')
        form = AuthenticationForm()
        return render(request, 'login.html', {'login_form': form})

    def post(self, request):
        if request.user.is_authenticated:
            redirect('main')
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('main')
        else:
            form = AuthenticationForm()
            return render(request, 'login.html', {'login_form': form, 'message': 'login failed!',})


class LogOutView(auth_views.LogoutView):
    def get(self, request):
        logout(request)
        return redirect("main")


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('main')
        form = UserCreationForm()
        return render(request, 'register.html', {'register_form': form})

    def post(self, request):
        if request.user.is_authenticated:
            redirect('main')
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = UserCreationForm()
            return render(request, 'register.html', {'register_form': form, 'message': 'Register failed!',})

        return redirect('main')
