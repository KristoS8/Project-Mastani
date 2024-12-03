from django.shortcuts import render, redirect

# Create your views here.

def dashboard (request):
    if request.user.is_authenticated:
        user = request.user

    else:
        user = None

    return render(request, 'seller_app/dashboard.html', {'user':user})

