# from django.shortcuts import redirect, render
# from django.urls import reverse
# from wallet.forms import UserForm, UserProfileInfoForm
# from django.contrib.auth import authenticate, login, logout, get_user_model
# from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.views.decorators.csrf import csrf_protect
# from .models import User, UserProfileInfo,Transaction


# def index(request):
#     return render(request, 'wallet/index.html')


# @login_required
# def special(request):
#     return HttpResponse("You are logged in. Nice!")


# @login_required
# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('index'))


# def register(request):
#     registered = False

#     if request.method == 'POST':
#         user_form = UserForm(request.POST)
#         profile_form = UserProfileInfoForm(request.POST)

#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save(commit=False)
#             user.set_password(user.password)
#             user.save()

#             profile = profile_form.save(commit=False)
#             profile.user = user

#             if 'profile_pic' in request.FILES:
#                 profile.profile_pic = request.FILES['profile_pic']

#             profile.save()

#             registered = True
#             messages.success(request, 'Registration successful. Please log in.')
#             return redirect('wallet:user_login')
#         else:
#             messages.error(request, 'Registration failed. Please correct the errors.')
#             print(user_form.errors, profile_form.errors)
#     else:
#         user_form = UserForm()
#         profile_form = UserProfileInfoForm()

#     return render(request, 'wallet/registration.html', {
#         'user_form': user_form,
#         'profile_form': profile_form,
#         'registered': registered
#     })


# @csrf_protect
# def user_login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         user = authenticate(request, email=email, password=password)

#         if user:
#             # Check if the account is active
#             if user.is_active:
#                 # Log the user in.
#                 login(request, user)
#                 # Send the user back to some page.
#                 # In this case their homepage.
#                 return render(request, 'wallet/dashboard.html', {})
#             else:
#                 # If the account is not active:
#                 return HttpResponse("Your account is not active.")
#         else:
#             print("Someone tried to login and failed.")
#             print("They used email: {} and password: {}".format(email, password))
#             return HttpResponse("Invalid login details supplied." + email + " " + password)

#     else:
#         # Nothing has been provided for username or password.
#         return render(request, 'wallet/login.html', {})


# @login_required
# def dashboard(request):
#     try:
#         profile = UserProfileInfo.objects.get(user_id=request.user)
#         coin_balance = profile.coin_balance
#         point_balance = profile.point_balance
#     except UserProfileInfo.DoesNotExist:
#         coin_balance = 0.0
#         point_balance = 0.0

#     context = {
#         'coin_balance': coin_balance,
#         'point_balance': point_balance
#     }

#     return render(request, 'wallet/dashboard.html', context)


# @login_required
# def user_list(request):
#     if request.method == 'POST':
#         recipient_id = request.POST.get('recipient')
#         points = float(request.POST.get('points'))

#         try:
#             user = get_user_model().objects.get(id=recipient_id)
#             recipient_profile = UserProfileInfo.objects.get(user_id=user.id)
#             recipient_profile.point_balance += points
#             recipient_profile.save()

#             # Create a record of the points awarded
#             transaction = Transaction.objects.create(recipient=user, points=points)
#             # Perform any additional actions related to the transaction

#             # Fetch the updated user list
#             users = UserProfileInfo.objects.all()
#             user_data = []
#             for user in users:
#                 user_data.append({
#                     'email': user.user.email,
#                     'id':user.profile_id,
#                     'first_name': user.first_name,
#                     'last_name': user.last_name,
#                     'point_balance': user.point_balance,
#                 })

#             # Return the updated user list as JSON response
#             return JsonResponse({'users': user_data})

#         except (get_user_model().DoesNotExist, UserProfileInfo.DoesNotExist):
#             # Handle the case when the user or recipient profile does not exist
#             pass
#     transactions = Transaction.objects.all()
#     users = UserProfileInfo.objects.all()
#     context = {
#         'users': users,
#         'transactions': transactions
#     }
#     return render(request, 'wallet/user_list.html', context)

# def store_transaction(request):
#     if request.method == 'POST' and request.is_ajax():
#         recipient = request.POST.get('recipient')
#         points = float(request.POST.get('points'))
#         date = request.POST.get('date')
#         time = request.POST.get('time')

#         # Update the recipient's point balance in the database
#         user = User.objects.get(email=recipient)
#         user.point_balance += points
#         user.save()

#         return JsonResponse({'success': True})
#     else:
#         return JsonResponse({'success': False, 'message': 'Invalid request'})
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from wallet.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponseForbidden, HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.views import View
from .models import User, UserProfileInfo, Transaction
from django.utils.decorators import method_decorator

class IndexView(View):
    def get(self, request):
        return render(request, 'wallet/index.html')

class SpecialView(View):
    @method_decorator(login_required)
    def get(self, request):
        return HttpResponse("You are logged in. Nice!")

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('wallet:index'))

class RegisterView(View):
    def get(self, request):
        registered = False
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        return render(request, 'wallet/registration.html', {
            'user_form': user_form,
            'profile_form': profile_form,
            'registered': registered
        })

    def post(self, request):
        registered = False

        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Check if a user with the same first and last name exists
            email = user_form.cleaned_data['email']
            first_name = profile_form.cleaned_data['first_name']
            last_name = profile_form.cleaned_data['last_name']

            if User.objects.filter(email=email).exists() or UserProfileInfo.objects.filter(first_name=first_name,last_name=last_name).exists():
                messages.error(request, 'A user with the same first name, last name, or email already exists.')
            else:
                user = user_form.save(commit=False)
                user.set_password(user.password)
                user.save()

                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()

                registered = True
                messages.success(request, 'Registration successful. Please log in.')
                return redirect('wallet:user_login')

        else:
            messages.error(request, 'Registration failed. Please correct the errors.')
            print(user_form.errors, profile_form.errors)

        return render(request, 'wallet/registration.html', {
            'user_form': user_form,
            'profile_form': profile_form,
            'registered': registered
        })


class UserLoginView(View):
    def get(self, request):
        return render(request, 'wallet/login.html', {})

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user:
            if user.is_active:
                login(request, user)
                if user.is_superuser:
                    return render(request, 'wallet/dashboard.html', {})
                else:
                    return render(request,'wallet/userDashboard.html',{})
            else:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used email: {} and password: {}".format(email, password))
            return HttpResponse("Invalid login details supplied." + email + " " + password)

class DashboardView(View):
    @method_decorator(login_required)
    def get(self, request):
        if request.user.is_superuser:
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
        else:
            response_data = {'message': 'You do not have permission to access this page.'}
            return JsonResponse(response_data, status=403)

class UserListView(View):
    @method_decorator(login_required)
    def get(self, request):
        if request.user.is_superuser:
            try:
                user_profile = UserProfileInfo.objects.get(user=request.user)
                transactions = Transaction.objects.all
            except UserProfileInfo.DoesNotExist:
                transactions = []

            users = UserProfileInfo.objects.all()
            context = {
                'users': users,
                'transactions': transactions,
            }
            return render(request, 'wallet/user_list.html', context)
        else:
            return HttpResponseForbidden("You do not have permission to access this page.")

class UserListView(View):
    @method_decorator(login_required)
    def get(self, request):
        if request.user.is_superuser:
            try:
                transactions = Transaction.objects.all()
                users = UserProfileInfo.objects.all()
                userT=User.objects.all()
            except UserProfileInfo.DoesNotExist:
                transactions = []

            
            context = {
                'users': users,
                'transactions': transactions,
                'userT':userT,
            }
            return render(request, 'wallet/user_list.html', context)
        else:
            return HttpResponseForbidden("You do not have permission to access this page.")

    @method_decorator(csrf_protect)
    def post(self, request):
        recipient_id = request.POST.get('recipient')
        sender_id = request.POST.get('sender')
        points = float(request.POST.get('points'))

        try:
            recipient = get_user_model().objects.get(id=recipient_id)
            sender = get_user_model().objects.get(id=sender_id)  # Corrected this line

            recipient_profile = UserProfileInfo.objects.get(user_id=recipient.id)
            sender_profile = UserProfileInfo.objects.get(user_id=sender.id)  # Corrected this line
                
            recipient_profile.point_balance += points
            recipient_profile.save()

            transaction = Transaction.objects.create(recipient=recipient, sender=sender, points=points)

            users = UserProfileInfo.objects.all()
            user_data = []
            for user in users:
                full_name = f"{user.first_name} {user.last_name}"
                user_data.append({
                    'email': user.user.email,
                    'id': user.profile_id,
                    'name':full_name,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'point_balance': user.point_balance,
                })

            return JsonResponse({'users': user_data})

        except (get_user_model().DoesNotExist, UserProfileInfo.DoesNotExist):
            pass


class StoreTransactionView(View):
    def post(self, request):
        if request.is_ajax():
            recipient = request.POST.get('recipient')
            points = float(request.POST.get('points'))
            date = request.POST.get('date')
            time = request.POST.get('time')

            user = User.objects.get(email=recipient)
            user.point_balance += points
            user.save()

            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid request'})


class UserDashboardView(View):
    @method_decorator(login_required)
    def get(self, request):
        try:
            profile = UserProfileInfo.objects.get(user_id=request.user)
            first_name=profile.first_name
            coin_balance = profile.coin_balance
            point_balance = profile.point_balance
        except UserProfileInfo.DoesNotExist:
            coin_balance = 0.0
            point_balance = 0.0

        context = {
            'coin_balance': coin_balance,
            'point_balance': point_balance,
            'first_name':first_name
        }
        return render(request, 'wallet/userDashboard.html',context)
    
class PointsDashboardView(View):
    @method_decorator(login_required)
    def get(self, request):
        try:
            
            profile = UserProfileInfo.objects.get(user_id=request.user)
            coin_balance = profile.coin_balance
            point_balance = profile.point_balance
            first_tname = profile.first_name
            last_name = profile.last_name
            user_profile = UserProfileInfo.objects.get(user=request.user)
            transactions = Transaction.objects.filter(recipient=user_profile.user)
        except UserProfileInfo.DoesNotExist:
            coin_balance = 0.0
            point_balance = 0.0
            transactions = []
            
        
        context = {
            'coin_balance': coin_balance,
            'point_balance': point_balance,
            'first_name':first_tname,
            'last_name':last_name,
            'transactions': transactions,
        }


        return render(request, 'wallet/pdash.html', context)