# Generated by Django 5.1.3 on 2024-11-23 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0008_withdraw_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dashboard',
            old_name='Deposit_Wallet_Balance',
            new_name='deposit_wallet_balance',
        ),
        migrations.RenameField(
            model_name='dashboard',
            old_name='Interest_Wallet_Balance',
            new_name='interest_wallet_balance',
        ),
        migrations.RenameField(
            model_name='dashboard',
            old_name='Referral_balance',
            new_name='referral_balance',
        ),
        migrations.RenameField(
            model_name='dashboard',
            old_name='Total_Deposit',
            new_name='total_deposit',
        ),
        migrations.RenameField(
            model_name='dashboard',
            old_name='Total_Withdraw',
            new_name='total_withdraw',
        ),
    ]
