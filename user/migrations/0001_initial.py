# Generated by Django 3.0.2 on 2020-02-29 22:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Credit_Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cc_number', models.CharField(max_length=30)),
                ('cc_expiration', models.CharField(max_length=10)),
                ('cc_security_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_address', models.ManyToManyField(related_name='home_address', to='user.Address')),
                ('payment_info', models.ManyToManyField(to='user.Credit_Card')),
                ('shipping_address', models.ManyToManyField(related_name='shipping_address', to='user.Address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
