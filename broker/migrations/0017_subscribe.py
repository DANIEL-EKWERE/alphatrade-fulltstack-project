# Generated by Django 5.1.3 on 2024-11-25 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0016_deposit_cryptomus_uuid_alter_deposit_wallet_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]