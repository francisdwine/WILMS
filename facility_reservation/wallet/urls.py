from django.urls import path
from wallet.views import IndexView, RegisterView, UserLoginView, DashboardView, UserListView, StoreTransactionView,UserLogoutView,UserDashboardView,PointsDashboardView, TransactionApprovalView,SuccessRedirectView,CoinTransactionCreateAndDashboardView,GetTransactionDetailsView,SettingsView,ChangePasswordView

# Increment 2
from django.conf import settings
from django.conf.urls.static import static  

from django.contrib.auth import views as auth_views

from . import views

app_name = 'wallet'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user_login/', UserLoginView.as_view(), name='user_login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),  
    path('user_list/', UserListView.as_view(), name='userlist'),
    path('store_transaction/', StoreTransactionView.as_view(), name='store_transaction'),
    path('logout/',UserLogoutView.as_view(),name='logout'),
    path('usrdashboard/', UserDashboardView.as_view(), name='usrdashboard'), 
    path('pdash/',PointsDashboardView.as_view(),name='pointsdash'),
    # INCREMENT 2
    path('createCoin/', CoinTransactionCreateAndDashboardView.as_view(), name='create-coin-transaction'),
    
    path('request/approval/', TransactionApprovalView.as_view(), name='request-approval'),
    path('success/',SuccessRedirectView.as_view(),name='success'),

    path('request/approval/approve-transaction/', views.approve_transaction, name='approve-transaction'),
    path('request/approval/deny-transaction/', views.deny_transaction, name='deny-transaction'),
    path('request/approval/get-transaction-details/', GetTransactionDetailsView.as_view(), name='get_transaction_details'),

    # INCREMENT 3
    path('settings/',SettingsView.as_view(),name='settings'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


