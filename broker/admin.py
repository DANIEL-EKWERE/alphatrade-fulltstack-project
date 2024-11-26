from django.contrib import admin
from broker.models import Account, Dashboard,Histotry,Withdraw,Deposit,Investment,Subscribe
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name = 'Account'


class CustomizedUserAdmin (UserAdmin):
    inlines = (AccountInline,)

admin.site.unregister(User)
admin.site.register(User,)
admin.site.register(Account)
# admin.site.register(Dashboard)
admin.site.register(Histotry)
# admin.site.register(Withdraw)
# admin.site.register(Deposit)
# admin.site.register(Investment)
admin.site.register(Subscribe)

@admin.register(Deposit)
class AdminDeposit(admin.ModelAdmin):
    list_display = [
        'user',
        'amount',
        'wallet_Address',
        'cryptomus_uuid',
        'status',
        'date',

    ]

@admin.register(Withdraw)
class AdminWithdraw(admin.ModelAdmin):
    list_display = [
        'user',
        'amount',
        'wallet_Address',
        'status',
        'date',

    ]

@admin.register(Dashboard)
class AdminDashboard(admin.ModelAdmin):
    list_display = [
        'user',
        'deposit_wallet_balance',
        'interest_wallet_balance',
        'total_invest_balance',
        'total_withdraw',
        'referral_balance',
        'referral_code',
        'date',

    ]

@admin.register(Investment)
class AdminInvestment(admin.ModelAdmin):
    list_display = [
        'user',
        'capital',
        'daily',
        'weekly',
        'monthly',

    ]
