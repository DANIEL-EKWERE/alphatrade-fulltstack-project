# Generated by Django 5.1.3 on 2024-11-22 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0007_deposit_status_histotry_ttype'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdraw',
            name='status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('DECLINED', 'DECLINED'), ('APPROVED', 'APPROVED')], default='PENDING', max_length=50),
        ),
    ]
