from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from wallet.forms import UserForm, UserProfileInfoForm,CoinTransactionForm, TransactionApprovalForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponseForbidden, HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from .decorators import superuser_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.views import View
from .models import User, UserProfileInfo, Transaction,CoinTransaction
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
import logging

# added increment 2
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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
    
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++INCREMENT2++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class CoinTransactionCreateAndDashboardView(LoginRequiredMixin, View):
    model = CoinTransaction
    form_class = CoinTransactionForm
    template_name = 'wallet/cointransaction_create_and_dashboard.html'
    success_url = reverse_lazy('wallet:coin-transaction-create')
    success_message = "Transaction was successfully created."

    def get(self, request, *args, **kwargs):
        try:
            profile = UserProfileInfo.objects.get(user_id=request.user)
            coin_balance = profile.coin_balance
            first_tname = profile.first_name
            last_name = profile.last_name
        except UserProfileInfo.DoesNotExist:
            coin_balance = 0.0

        form = CoinTransactionForm(user=request.user)
        coin_transactions = CoinTransaction.objects.filter(requestee=request.user)

        context = {
            'form': form,
            'coin_balance': coin_balance,
            'first_name': first_tname,
            'last_name': last_name,
            'coin_transactions': coin_transactions,
        }

        return render(request, 'wallet/cointransaction_create_and_dashboard.html', context)

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        return response

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = self.request.user
            form.save()
            messages.success(request, self.success_message)
            response_data = {
                'status': 'success',
                'message': 'Form submitted successfully.',
            }
        else:
            # If the form is invalid, show the errors to the user.
            messages.error(request, "Form is not valid. Please check the fields.")
            response_data = {
                'status': 'fail',
                'message': 'Form submission failed. Please check the fields.',
                'errors': form.errors,
            }
        
        # Return a JSON response with the appropriate status and message
        return JsonResponse(response_data)



@method_decorator(login_required, name='dispatch')
class TransactionApprovalView(View):
    template_name = 'wallet/transaction_approval.html'
    form_class = TransactionApprovalForm

    def get(self, request):
        if request.user.is_superuser:
            transactions = CoinTransaction.objects.all()
            return render(request, self.template_name, {'transactions': transactions, 'form': self.form_class()})
        else:
            return HttpResponseForbidden("You do not have permission to access this page.")
        


    

class SuccessRedirectView(View):
    def get(self, request):
        return redirect('wallet/success')
    


# Custom user test function to check if the user is a superuser
def is_superuser(user):
    return user.is_superuser

@login_required
@user_passes_test(is_superuser)
def approve_transaction(request):
    if request.method == 'POST':
        reference_code = request.POST.get('reference_code')

        # Fetch the transaction by reference code and update its status and requestee's balance
        try:
            transaction = CoinTransaction.objects.get(reference_code=reference_code)
            if not transaction.is_completed:
                transaction.is_completed = True
                transaction.is_denied = False
                transaction.save()

                # Update the requestee's coin balance here
                requestee_profile = UserProfileInfo.objects.get(user=transaction.requestee)
                requestee_profile.coin_balance += transaction.amount
                requestee_profile.save()

                # Return a success response
                return JsonResponse({"status": "success", "message": "Transaction approved successfully."})

        except CoinTransaction.DoesNotExist:
            pass

    # If the transaction approval fails or it's not a POST request, return an error response
    return JsonResponse({"status": "fail", "message": "Transaction approval failed."})

@login_required
@user_passes_test(is_superuser)
def deny_transaction(request):
    if request.method == 'POST':
        reference_code = request.POST.get('reference_code')

        # Fetch the transaction by reference code and update its status
        try:
            transaction = CoinTransaction.objects.get(reference_code=reference_code)
            if not transaction.is_denied:
                transaction.is_completed = False
                transaction.is_denied = True
                transaction.save()

                # Return a success response
                return JsonResponse({"status": "success", "message": "Transaction denied successfully."})

        except CoinTransaction.DoesNotExist:
            pass

    # If the transaction denial fails or it's not a POST request, return an error response
    return JsonResponse({"status": "fail", "message": "Transaction denial failed."})


class GetTransactionDetailsView(UserPassesTestMixin, View):
    def test_func(self):
        # Check if the user is a superuser
        return self.request.user.is_superuser

    def get(self, request):
        reference_code = request.GET.get('reference_code', None)

        # Fetch the transaction details by reference code
        try:
            transaction = CoinTransaction.objects.get(reference_code=reference_code)

            # Create a dictionary with the transaction details
            transaction_data = {
                'reference_code': transaction.reference_code,
                'requestee': transaction.requestee.email,  # Assuming 'requestee' is a ForeignKey to User
                'amount': transaction.amount,
                'date_in_receipt': transaction.date_in_receipt.strftime('%Y-%m-%d %H:%M:%S'),  # Format the date as desired
                'status': 'COMPLETED' if transaction.is_completed and not transaction.is_denied else 'DENIED' if transaction.is_denied and not transaction.is_completed else 'PENDING',
                'image_receipt_url': transaction.image_receipt.url,
            }

            return JsonResponse(transaction_data)
        except CoinTransaction.DoesNotExist:
            pass

        # If the transaction details retrieval fails or it's not a valid GET request, return an error response
        return JsonResponse({'status': 'fail', 'message': 'Transaction details retrieval failed.'})

