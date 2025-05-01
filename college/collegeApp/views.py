from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib import messages
# from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
User = get_user_model()
def user_register(request):
    if request.method == 'POST':
        # email = request.POST['email']
        # username = request.POST['username']
        # password = request.POST['password_original']
        # password_confirm = request.POST['password_confirm']
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password_original')
        password_confirm = request.POST.get('password_confirm')

        # Check if passwords match
        if password != password_confirm:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        # Check if username or email already exists
        if User.objects.filter(username1=username).exists():
            messages.error(request, "Username is already taken.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('register')

        # Create the user
        user = User.objects.create_user(username1=username, email=email, password=password)
        user.save()

        messages.success(request, "Registration successful! You can now log in.")
        return redirect('login')  # Adjust to your login route

    else:
        return render(request, 'register.html')
def Login(request):
    if request.user.is_authenticated:
        return redirect('user_profile')
        
    if request.method == "POST":
        username_or_email = request.POST.get("username")
        password = request.POST.get("password")

        # Try to find user by username1 or email
        user_obj = User.objects.filter(username1=username_or_email).first() or \
                  User.objects.filter(email=username_or_email).first()

        if user_obj:
            if check_password(password, user_obj.password):
                login(request, user_obj)
                messages.success(request, f"Welcome back, {user_obj.username1}!")
                next_url = request.GET.get('next', 'user_profile')
                return redirect(next_url)
            messages.error(request, "Incorrect password.")
        else:
            messages.error(request, "User not found.")

    return render(request, 'login.html', {'next': request.GET.get('next', '')})
# def Login(request):
#     if request.method == "POST":
#         username_or_email = request.POST.get("username")
#         password = request.POST.get("password")

#         try:
#             user_obj = User.objects.get(username1=username_or_email)
#         except User.DoesNotExist:
#             try:
#                 user_obj = User.objects.get(email=username_or_email)
#             except User.DoesNotExist:
#                 user_obj = None

#         if user_obj:
#             user = authenticate(request, username1=user_obj.username, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('/')
#             else:
#                 messages.error(request, "Incorrect password.")
#         else:
#             messages.error(request, "User not found.")

#         return render(request, 'login.html')  # <-- Fix here
#     return render(request, 'login.html')

def signout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')  # Or wherever your login page is
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')  # or wherever you want to redirect after saving
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'edit_profile.html', {'form': form})
# @login_required
@login_required(login_url='login')
def user_profile(request):
    user = request.user
    form = UserProfileForm(instance=user)  # Populate form with current user data
    # print(form)
    
    return render(request, 'user_profile.html', {'form': form, 'user': user})


def meeting_Details(request):
    return render(request,"meeting-details.html")

def singup_page(request):
    return render(request,"register.html")

def meetings(request):
    return render(request,"meetings.html")

def results(request):
    course_query = request.GET.get('course', '').strip()
    reg_query = request.GET.get('registration', '').strip()

    users = User.objects.all()

    if course_query:
        users = users.filter(course__icontains=course_query)

    if reg_query:
        users = users.filter(registration__icontains=reg_query)

    return render(request, "results.html", {
        "users": users,
        "course_query": course_query,
        "reg_query": reg_query,
    })

def search_user(request):
    course = request.GET.get('course')
    registration = request.GET.get('registration')

    users = []
    if course and registration:
        users = User.objects.filter(course__icontains=course, registration__icontains=registration)

    return render(request, 'search.html', {
        'course': course,
        'registration': registration,
        'users': users
    })


def login_page(request):
    return render(request,"login.html")
def collegeIndex(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Optional: Validate fields manually if needed
        if name and email and subject and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('/')
        else:
            messages.error(request, 'Please fill in all required fields.')

    return render(request, 'index.html')