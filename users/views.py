from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *

# Create your views here.

def profiles(request):

    profiles = Profile.objects.all()
    context = {'profiles': profiles}

    return render(request, 'users/profile.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile':profile}

    return render(request, 'users/user-profile.html', context)




