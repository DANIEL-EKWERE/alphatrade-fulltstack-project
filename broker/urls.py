from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('deposit/', deposit, name='deposit'),
    path('depositcrypto/', depositcrypto, name='deposit-crypto'),
    path('withdraw/', withdraw, name='withdraw'),
    path('withdrawcrypto/', withdrawcrypto, name='withdraw-crypto'),
    path('plans/', plans, name='plans'),

    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('resetpassword/', resetpassword, name='reset-password'),
    path('contact/', contactus, name='contact'),
    path('about/', about, name='about'),
    path('transaction/', transaction, name='transaction'),
    path('signout/', signout, name='sign-out'),
    path('investment/', investment, name='investment'),
    # path('', include('broker.urls')),
]