from django.shortcuts import render, redirect
from ..forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def logout_request(request) :
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("main")
