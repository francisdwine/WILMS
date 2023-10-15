from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from urllib.parse import urlencode
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import VendorTransaction
from .serializers import UserSerializer, VendorTransactionSerializer
from django.views.generic import TemplateView
from django.contrib.auth import logout

from wallet.models import UserProfileInfo
from rest_framework.authtoken.models import Token

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.utils.decorators import method_decorator
from rest_framework.decorators import authentication_classes, permission_classes


from django.shortcuts import render, redirect
from urllib.parse import urlencode  # Import urlencode to encode URL parameters

@api_view(['GET', 'POST'])
def login_view(request):
    if request.method == 'GET':
        # Serve the login form
        return render(request, 'login.html')

    elif request.method == 'POST':
        # Handle the login POST request
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email and password:
            user = authenticate(request, email=email, password=password)
            if user:
                # Log the user in
                login(request, user)
                # Generate or retrieve an authentication token
                token, _ = Token.objects.get_or_create(user=user)

                # Encode the token as a query parameter
                token_param = urlencode({'token': token.key})

                # Redirect the user to the create transaction page with the token parameter
                redirect_url = f'/walletAPI/create-transaction/?{token_param}'
                return redirect(redirect_url)
        
        return JsonResponse({'detail': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)





class CreateVendorTransactionView(generics.CreateAPIView):
    queryset = VendorTransaction.objects.all()
    serializer_class = VendorTransactionSerializer
    permission_classes = [IsAuthenticated]  # Require authentication

    def get(self, request, *args, **kwargs):
        # Serve the HTML form for creating a VendorTransaction
        return render(request, 'create-transaction.html')

    def perform_create(self, serializer):
        # Get the authenticated user
        user = self.request.user

        # Get the selected currency from the form data
        currency = self.request.data.get('currency')

        # Get the transaction amount from the form data
        transaction_amount = float(self.request.data.get('transaction_amount'))

        # Assuming there's a one-to-one relationship between User and UserProfileInfo
        # Retrieve the user's UserProfileInfo
        profile_info = UserProfileInfo.objects.get(user=user)

        if currency == 'coins':
            # Deduct the amount from the user's coin_balance in UserProfileInfo
            if profile_info.coin_balance >= transaction_amount:
                profile_info.coin_balance -= transaction_amount
                profile_info.save()
            else:
                return Response({'detail': 'Insufficient coins.'}, status=status.HTTP_400_BAD_REQUEST)
        elif currency == 'points':
            # Deduct the amount from the user's point_balance in UserProfileInfo
            if profile_info.point_balance >= transaction_amount:
                profile_info.point_balance -= transaction_amount
                profile_info.save()
            else:
                return Response({'detail': 'Insufficient points.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create the VendorTransaction instance with the user as the customer
        serializer.save(customer=user)

    def post(self, request, *args, **kwargs):
        # Handle the creation of the VendorTransaction
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # Prepare the data to be passed to the receipt template
        receipt_data = {
            'reference_code': serializer.data['reference_code'],
            'transaction_date': serializer.data['transaction_date'],
            'description': serializer.data['description'],
            'transaction_id': serializer.data['transaction_id'],
            'transaction_amount': serializer.data['transaction_amount'],
            'currency': self.request.data.get('currency'),  # Include the selected currency
        }

        # Render the receipt template with the receipt data
        receipt_html = render(request, 'receipt.html', receipt_data)

        # Response data
        response_data = {
            'message': 'VendorTransaction created successfully',
            'reference_code': serializer.data['reference_code'],
            'user_id': self.request.user.id,  # Assuming you want to include the user ID
            'receipt_html': receipt_html.content.decode(),
        }

        return HttpResponse(receipt_html.content)
    

class TransactionReceiptView(TemplateView):
    template_name = 'receipt.html'


def logout_view(request):
    # Use Django's logout function to log the user out and clear the session
    logout(request)
    
    # Redirect the user to the login page or any other desired destination
    return redirect('walletAPI:login')  # Replace 'login' with the name of your login 
