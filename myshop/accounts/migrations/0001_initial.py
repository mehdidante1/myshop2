# Generated by Django 3.2.6 on 2021-11-08 22:29

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='نام')),
                ('last_name', models.CharField(max_length=150, verbose_name='نام خانوادگی')),
                ('national_code', models.CharField(max_length=40, verbose_name='کد ملی')),
                ('mobile_number', models.CharField(max_length=100, verbose_name='شماره موبایل')),
                ('email', models.EmailField(max_length=200, verbose_name='آدرس الکترونیکی')),
                ('pay_number', models.CharField(max_length=100, verbose_name='شماره کارت')),
                ('profile_image', models.ImageField(upload_to='profile_user/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]