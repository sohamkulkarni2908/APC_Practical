from django.shortcuts import render

from .forms import LoginForm

def login_view(request):
    message = ""

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            if username == "admin" and password == "1234":
                message = "Login Successful !"

            else:
                message = "Invalid Username or password!"

    else:
            form = LoginForm()

    return render(request, "login.html",{
            "form" : form,
            "message" : message
        })