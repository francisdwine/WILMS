from django.shortcuts import redirect, render
from django.urls import reverse
from wallet.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .models import User, UserProfileInfo,Transaction


def index(request):
    return render(request, 'wallet/index.html')


@login_required
def special(request):
    return HttpResponse("You are logged in. Nice!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('wallet:user_login')
        else:
            messages.error(request, 'Registration failed. Please correct the errors.')
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'wallet/registration.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    })


@csrf_protect
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user:
            # Check if the account is active
            if user.is_active:
                # Log the user in.
                login(request, user)
                # Send the user back to some page.
                # In this case their homepage.
                return render(request, 'wallet/dashboard.html', {})
            else:
                # If the account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used email: {} and password: {}".format(email, password))
            return HttpResponse("Invalid login details supplied." + email + " " + password)

    else:
        # Nothing has been provided for username or password.
        return render(request, 'wallet/login.html', {})


@login_required
def dashboard(request):
    try:
        profile = UserProfileInfo.objects.get(user_id=request.user)
        coin_balance = profile.coin_balance
        point_balance = profile.point_balance
    except UserProfileInfo.DoesNotExist:
        coin_balance = 0.0
        point_balance = 0.0

    context = {
        'coin_balance': coin_balance,
        'point_balance': point_balance
    }

    return render(request, 'wallet/dashboard.html', context)


@login_required
def user_list(request):
    if request.method == 'POST':
        recipient_id = request.POST.get('recipient')
        points = float(request.POST.get('points'))

        try:
            user = get_user_model().objects.get(id=recipient_id)
            recipient_profile = UserProfileInfo.objects.get(user_id=user.id)
            recipient_profile.point_balance += points
            recipient_profile.save()

            # Create a record of the points awarded
            transaction = Transaction.objects.create(recipient=user, points=points)
            # Perform any additional actions related to the transaction

            # Fetch the updated user list
            users = UserProfileInfo.objects.all()
            user_data = []
            for user in users:
                user_data.append({
                    'email': user.user.email,
                    'id':user.profile_id,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'point_balance': user.point_balance,
                })

            # Return the updated user list as JSON response
            return JsonResponse({'users': user_data})

        except (get_user_model().DoesNotExist, UserProfileInfo.DoesNotExist):
            # Handle the case when the user or recipient profile does not exist
            pass
    transactions = Transaction.objects.all()
    users = UserProfileInfo.objects.all()
    context = {
        'users': users,
        'transactions': transactions
    }
    return render(request, 'wallet/user_list.html', context)

def store_transaction(request):
    if request.method == 'POST' and request.is_ajax():
        recipient = request.POST.get('recipient')
        points = float(request.POST.get('points'))
        date = request.POST.get('date')
        time = request.POST.get('time')

        # Update the recipient's point balance in the database
        user = User.objects.get(email=recipient)
        user.point_balance += points
        user.save()

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request'})