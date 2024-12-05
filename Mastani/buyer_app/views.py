from django.shortcuts import render,redirect
from auth_user.models import CustomUser
from .forms import UpdateUser
from django.contrib import messages

# Create your views here.

def profile_view (request):    
    # update user data

    user_auth = request.user

    if request.method == 'POST':
        form = UpdateUser(request.POST, instance=user_auth)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile Anda Telah Di Perbaharui!')
            return redirect('profile_view')
    else:
        form = UpdateUser(instance=user_auth)

    return render(request, "buyer_app/profile.html", {'form':form})