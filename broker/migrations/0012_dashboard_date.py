# Generated by Django 5.1.3 on 2024-11-23 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0011_alter_dashboard_deposit_wallet_balance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='date',
            field=models.DateField(auto_now_add=True, default='2024-11-24'),
            preserve_default=False,
        ),
    ]
