from wallet import views
from django.urls import path

app_name= 'wallet'

urlpatterns = [
    # path("",views.home, name="home"),
    path('',views.index,name='index'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user_list/', views.user_list, name='userlist'),
    path('store_transaction/', views.store_transaction, name='store_transaction'),
]