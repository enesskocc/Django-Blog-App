from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth import logout, login
from .forms import UserForm, UserProfileForm, UserUpdateProfile
from .models import  UserProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    form_user = UserForm(request.POST or None)

    if form_user.is_valid():
        user = form_user.save()
        login(request, user)
        messages.success(request, 'Successfully Registered!')
        return redirect('list')

    context = {
    'form_user' : form_user
    }

    return render(request, 'user/register.html', context)


def user_login(request):
    form = AuthenticationForm(request, request.POST or None)

    if form.is_valid():
        user =  form.get_user()
        if user:
            login(request, user)
            messages.success(request, 'Successfully Login!')
            return redirect('list')

    context = {
        'form' : form
    }

    return render(request, 'user/login.html', context)

def user_logout(request):
    logout(request)
    messages.success(request, 'Successfully Logout!')
    # return redirect('logout')

    return render(request, 'user/logout.html')

def user_profile(request):
    userinfo = get_object_or_404(User, username=request.user) ## databasen user bilgilerini(username ile yakaliyoruz) getiriyor!
    # userprofileinfo = get_object_or_404(UserProfile, user = userinfo) ## yakaladigimiz user'Den userprofil bilgilerini getiriyoruz.
    # profil = UserProfileForm(instance=userprofileinfo)
    form_user = UserUpdateProfile(instance=userinfo)
    if request.method == 'POST':
        form_user = UserUpdateProfile(request.POST, instance=userinfo)
        # profil = UserProfileForm(request.POST, request.FILES, instance=userprofileinfo)
        if form_user.is_valid():
            form_user.save()
            # profil.save()
            return redirect('list')


    context = {
        # 'profil': profil,
        'form_user': form_user
    }

    return render(request, 'user/profile.html', context)

