from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True  # Set the user as staff
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Now you can login!')
            return redirect('login')

        else:
            messages.warning(request, 'Unable to create account!')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'title': 'Student Registration'})
