from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from users.forms import SignUpForm


def signup(request):
    """
    Handle user signup and address creation.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirects to the 'index' page upon successful signup or
        renders the signup form if the request method is not POST.
    """
    if request.method == "POST":
        formset = SignUpForm(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect("index")
    else:
        formset = SignUpForm()
    context = {"formset": formset}
    return render(request, "users/signup.html", context)


def signin(request):
    """
    Handle user sign-in.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirects to the 'index' page upon successful sign-in or
        renders the sign-in form if the request method is not POST.
    """
    if request.method == "POST":
        formset = AuthenticationForm(data=request.POST)
        if formset.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect("index")
    else:
        formset = AuthenticationForm()
    context = {"formset": formset}
    return render(request, "users/login.html", context)


def logout_view(request):
    """
    Log the user out and redirect to the 'index' page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Redirects to the 'index' page after logging the user out.
    """
    logout(request)
    return redirect("index")
