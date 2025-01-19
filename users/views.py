from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def profiles(request):

    user = request.user
    if user.is_authenticated:
        test = user.get_user_permissions()
    
    print(f'the fullname is {test}')

    return render(request, 'users/profile.html')



