# Generated by Django 5.1.3 on 2024-11-23 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0009_rename_deposit_wallet_balance_dashboard_deposit_wallet_balance_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dashboard',
            old_name='Total_invest_Balance',
            new_name='referral_code',
        ),
        migrations.AddField(
            model_name='dashboard',
            name='total_invest_balance',
            field=models.IntegerField(default=0.0, max_length=50),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='deposit_wallet_balance',
            field=models.IntegerField(default=0.0, max_length=50),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='interest_wallet_balance',
            field=models.IntegerField(default=0.0, max_length=50),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='referral_balance',
            field=models.IntegerField(default=0.0, max_length=50),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='total_deposit',
            field=models.IntegerField(default=0.0, max_length=50),
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='total_withdraw',
            field=models.IntegerField(default=0.0, max_length=50),
        ),
    ]
