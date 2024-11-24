from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout,login, authenticate
from broker.models import Account, Dashboard, Histotry, Withdraw,Deposit, Investment,ContactUs
from django.contrib import messages
# Create your views here.


def index(request):
    user = request.user
    if user.is_authenticated:
        return redirect('/dashboard/')
    return render(request, 'index.html')

# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render
# from django.core.exceptions import ObjectDoesNotExist
# from your_app.models import Dashboard, History  # Replace `your_app` with the correct app name

@login_required
def dashboard(request):
    user = request.user

    # Initialize variables with default values
    details = None
    pending = None
    approved = None
    cancelled = None
    deposits = None
    withdraws = None
    profile = None

    try:
        # Fetch the Dashboard object for the user
        details = Dashboard.objects.get(user=user)

        # Fetch History objects based on transaction type
        # pending = Histotry.objects.filter(user=user, tType="PENDING")
        # approved = Histotry.objects.filter(user=user, tType="APPROVED")
        # cancelled = Histotry.objects.filter(user=user, tType="CANCELLED")

        deposits = Deposit.objects.filter(user=user).order_by("-date")
        withdraws = Withdraw.objects.filter(user=user)
        profile = Account.objects.get(user=user)
        
        # if withdraws.amount == 0.0:
        #     print(0)
        # else:
        #     print("its not")
    except ObjectDoesNotExist:
        # Handle case where Dashboard or related objects do not exist
        print("No Dashboard object or related data found for the user.",user)

    # Pass all required data to the template
    return render(
        request, 
        'dashboard.html', 
        {
            'details': details,
            'pending': pending,
            'approved': approved,
            'cancelled': cancelled,
            'deposits': deposits,
            'withdraws':withdraws,
            'profile':profile,
        }
    )


@login_required
def profile(request):
    user = request.user
    profile = Account.objects.get(user=user)

    return render(request, 'profile.html',{'profile':profile})

@login_required
def withdraw(request):
    return render(request, 'withdraw.html')

@login_required
def withdrawcrypto(request):
    user = request.user
    dashboard = None
    errors = []
    if request.method == "POST":
            amount = request.POST.get('amount')
            address = request.POST.get('copy')
            try:
                dashboard = Dashboard.objects.get(user=user)
                if int(dashboard.deposit_wallet_balance) < int(amount):
                    errors.append("your account balance is not sufficient to place this withdrawal")
                    return render(request, 'withdraw-crypto.html',{'errors':errors})
            except ObjectDoesNotExist:
                dashboard = None
            withdraw = Withdraw.objects.create(
                user=user,
                amount=amount,
                wallet_Address=address
            )

            history = Histotry.objects.create(
                user=user,
                amount=amount,
                wallet_Address=address,
                tType="Withdraw"
            )
            return redirect('/dashboard/')

    return render(request, 'withdraw-crypto.html')

@login_required
def deposit(request):
    return render(request, 'deposit.html')

@login_required
def depositcrypto(request):
    user = request.user
    if request.method == "POST":
        amount = request.POST.get('amount')
        address = request.POST.get('copy')

        deposit = Deposit.objects.create(
            user=user,
            amount=amount,
            wallet_Address=address
        )

        history = Histotry.objects.create(
            user=user,
            amount=amount,
            wallet_Address=address,
            tType="Deposit"
        )


        return redirect('/dashboard/')


    return render(request, 'deposit-crypto.html')

def signup(request):
    if request.method == 'POST':
        # Get form data
        username = request.POST.get('username')
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        password = request.POST.get('password')
        confirm_password = request.POST.get('ConfirmPassword')
        email = request.POST.get('email')
        country = request.POST.get('country')
        phone = request.POST.get('phone')
        referrer = request.POST.get('referrer')

        address = request.POST.get('aadress')
        state = request.POST.get('state')
        city = request.POST.get('city')
        zipcode = request.POST.get('zipCode')
       
        # Debug: Log all inputs
        print("Form Data:", username, first_name, last_name, email, phone, country, address, state, city,zipcode)

        # Validate input
        errors = []
        if password != confirm_password:
            errors.append("Passwords do not match.")
        if User.objects.filter(username=username).exists():
            errors.append("Username already exists.")
        if User.objects.filter(email=email).exists():
            errors.append("Email already exists.")
        if Account.objects.filter(phone=phone).exists():
            errors.append("Phone number already exists.")

         # Debug: Log errors
        print("Errors:", errors)

        if errors:
            # Return errors to the template
            return render(request, 'signup.html', {'errors': errors})

        # Create user and account if no errors
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        Account.objects.create(
            first_name = first_name,
            last_name=last_name,
            user=user,
            country=country,
            phone=phone,
            referral=referrer,
            address=address,
            city=city,
            state=state,
            zipcode=zipcode
        )
        Dashboard.objects.create(
            user=user,
            deposit_wallet_balance=10.0,
            interest_wallet_balance=0.0,
            total_invest_balance=0.0,
            total_deposit=0.0,
            total_withdraw=0.0,
            referral_balance=0.0,
            referral_code=referrer

        )
        # Deposit.objects.create(user=user,amount=0.0,wallet_Address="N/A",status="PENDING")
        # Withdraw.objects.create(user=user,amount=0.0,wallet_Address="N/A",status="PENDING")


        login(request, user)
        return redirect('/dashboard/')

    # Render the signup form
    return render(request, 'signup.html')

def signin(request):

    if request.method == 'POST':
        # Get form data
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user=user)
            messages.success(request,"login successful")
            return render(request, 'dashboard.html')
    messages.error(request,"login not successful, check details and try again.")
    return render(request, 'signin.html')

def resetpassword(request):
    return render(request, 'reset-password.html')


def plans(request):
    return render(request, 'plans.html')

def privacyPolicy(request):
    return render(request, 'privacy-policy.html')

def licensing(request):
    return render(request, 'licensing.html')

def contactus(request):
    if request.method == "POST":
        fullName = request.POST.get("fullName")
        email = request.POST.get("email")
        message = request.POST.get("Message")

        ContactUs.objects.create(
            full_name=fullName,
            email=email,
            message=message
        )
        return redirect("/")

    return render(request, 'contact.html')

def about(request):
    return render(request, 'aboutus.html')

# def signup(request):

#     return render(request, 'signup.html')

@login_required
def transaction(request):
    user = request.user
    deposits = None
    withdraws = None
    try:
        history = Histotry.objects.filter(user=user)
        deposits = Deposit.objects.filter(user=user).order_by("-date")
        withdraws = Withdraw.objects.filter(user=user)
    except ObjectDoesNotExist:
        history = None

    return render(request, 'transaction.html',{'history':history,'deposits':deposits,'withdraws':withdraws})

@login_required
def investment(request):
    user = request.user
    investment = None
    try:
        investment = Investment.objects.get(user=user)
    except ObjectDoesNotExist:
        investment = None
    return render(request, 'investment.html',{'investment':investment})

def signout(request):
    logout(request)
    return redirect('home')