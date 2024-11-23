# Generated by Django 5.1.3 on 2024-11-22 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0006_alter_dashboard_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('DECLINED', 'DECLINED'), ('APPROVED', 'APPROVED')], default='PENDING', max_length=50),
        ),
        migrations.AddField(
            model_name='histotry',
            name='tType',
            field=models.CharField(default='N/A', max_length=50),
        ),
    ]
