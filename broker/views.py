from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout,login, authenticate
from broker.models import Account, Dashboard, Histotry, Withdraw,Deposit
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
    deposit = None
    withdraw = None
    profile = None

    try:
        # Fetch the Dashboard object for the user
        details = Dashboard.objects.get(user=user)

        # Fetch History objects based on transaction type
        # pending = Histotry.objects.filter(user=user, tType="PENDING")
        # approved = Histotry.objects.filter(user=user, tType="APPROVED")
        # cancelled = Histotry.objects.filter(user=user, tType="CANCELLED")

        # deposit = Deposit.objects.filter(user=user)
        # withdraw = Withdraw.objects.filter(user=user)
        profile = Account.objects.get(user=user)
        print(profile)
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
            'deposit': deposit,
            'withdraw':withdraw,
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

    if request.method == "POST":
            amount = request.POST.get('amount')
            address = request.POST.get('copy')

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
            Deposit_Wallet_Balance=10.0,
            Interest_Wallet_Balance=0.0,
            Total_invest_Balance=0.0,
            Total_Deposit=0.0,
            Total_Withdraw=0.0,
            Referral_code=referrer

        )


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


def contactus(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'aboutus.html')

# def signup(request):

#     return render(request, 'signup.html')

@login_required
def transaction(request):
    user = request.user

    try:
        history = Histotry.objects.get(user=user)
    except ObjectDoesNotExist:
        history = None

    return render(request, 'transaction.html')

@login_required
def investment(request):
    return render(request, 'investment.html')

def signout(request):
    logout(request)
    return redirect('home')