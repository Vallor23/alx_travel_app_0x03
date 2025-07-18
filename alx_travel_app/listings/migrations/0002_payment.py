# Generated by Django 5.2.1 on 2025-06-29 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(choices=[('PENDING', 'Pending'), ('SUCCESS', 'Success'), ('FAILED', 'Failed')], default='PENDING', max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_id', models.CharField(max_length=100, unique=True)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='listings.booking')),
            ],
        ),
    ]
