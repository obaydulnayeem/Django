from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm, ProfileForm, EditProfileForm
from django.contrib.auth.decorators import login_required
from . models import Profile
from django.contrib.auth.models import User
from study.models import Department, Course
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            # UserProfile.objects.create(user=user)
            return redirect('home')  # Redirect to the user's profile page
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the user's profile page
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

# @login_required
# def profile(request):
#     try:
#         profile = request.user.profile  # Retrieve the user's profile
#     except Profile.DoesNotExist:
#         # If the profile does not exist, create a new one
#         profile = Profile(user=request.user)
#         profile.save()

#     return render(request, 'profile.html', {'profile': profile})



# from django.core.exceptions import ObjectDoesNotExist

# @login_required
# def profile(request):
#     try:
#         profile = request.user.profile  # Retrieve the user's profile
#     except ObjectDoesNotExist:
#         if request.method == 'POST':
#             form = ProfileForm(request.POST)
#             if form.is_valid():
#                 profile = form.save(commit=False)
#                 profile.user = request.user
#                 profile.save()
#                 return redirect('profile')  # Redirect to profile after creating it
#         else:
#             form = ProfileForm()
            
#         return render(request, 'profile.html', {'form': form})

#     return render(request, 'profile.html', {'profile': profile})


@login_required
def view_profile(request):
    # Assuming the user is logged in
    user = request.user
    
    try:
        profile = Profile.objects.get(user=user)  # Retrieve the user's profile
    except Profile.DoesNotExist:
         # If the profile doesn't exist, create a new one
        profile = Profile(user=user)
        profile.save()
        # You can also redirect the user to an edit profile page to fill in details
        return redirect('view_profile')
    
    context = {
        'profile': profile
    }

    return render(request, 'view_profile.html', context)


@login_required
def edit_profile(request):
    user = request.user

    try:
        profile = Profile.objects.get(user=user)  # Retrieve the user's profile
    except Profile.DoesNotExist:
        # If the profile doesn't exist, create a new one
        profile = Profile(user=user)
        profile.save()
    
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form
    }

    return render(request, 'edit_profile.html', context)


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})



def update_user_type(request, user_id):
    user = get_object_or_404(User, id=user_id)

    try:
        profile = user.profile  # Attempt to retrieve the profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=user)  # If the profile doesn't exist, create a new one

    if request.method == 'POST':
        new_user_type = request.POST.get('new_user_type')
        profile.user_type = new_user_type
        profile.save()
        return redirect('user_list')  # Redirect to the user list page after updating

    return render(request, 'update_user_type.html', {'profile': profile})




# AJAX
def load_departments(request):
    university_id = request.GET.get('university_id')
    departments = Department.objects.filter(university_id=university_id).all()
    return render(request, 'department_dropdown_list_options.html', {'departments': departments})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)