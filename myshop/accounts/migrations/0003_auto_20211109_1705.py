# Generated by Django 3.2.6 on 2021-11-10 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=200, verbose_name='آدرس الکترونیکی'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=100, verbose_name='شماره موبایل'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='national_code',
            field=models.CharField(blank=True, max_length=40, verbose_name='کد ملی'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pay_number',
            field=models.CharField(blank=True, max_length=100, verbose_name='شماره کارت'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='profile_user/'),
        ),
    ]
