from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegister
from django.contrib import messages

# Create your views here.
def main(request):
    return render(request,'main.html')

def register(request):
    if request.method == "POST":
        request_form = UserRegister(request.POST)
        if request_form.is_valid():
            user = request_form.save(commit=False)
            user.set_password(request_form.cleaned_data['password1'])
            user.save()
            messages.success(request, ("Registration has been completed successfully, login to proceed."))
    else:
        request_form = UserRegister()  # Define reg_form here
    return render(request,'register.html',{'reg_form':request_form})