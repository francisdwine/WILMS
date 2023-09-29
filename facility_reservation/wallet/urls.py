# from wallet import views
# from django.urls import path

# app_name= 'wallet'

# urlpatterns = [
#     # path("",views.home, name="home"),
#     path('',views.index,name='index'),
#     path('register/', views.register, name='register'),
#     path('user_login/', views.user_login, name='user_login'),
#     path('dashboard/', views.dashboard, name='dashboard'),
#     path('user_list/', views.user_list, name='userlist'),
#     path('store_transaction/', views.store_transaction, name='store_transaction'),
# ]

from django.urls import path
from wallet.views import IndexView, RegisterView, UserLoginView, DashboardView, UserListView, StoreTransactionView,UserLogoutView,UserDashboardView,PointsDashboardView

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
]
