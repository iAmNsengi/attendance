# Generated by Django 3.2.13 on 2022-06-28 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lecturer',
            fields=[
                ('sn', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Serial Number')),
                ('school', models.CharField(max_length=30, verbose_name='School')),
                ('department', models.CharField(max_length=30, verbose_name='Department')),
                ('firstname', models.CharField(max_length=50, verbose_name='First Name')),
                ('lastname', models.CharField(max_length=50, verbose_name='Last Name')),
                ('idnumber', models.CharField(max_length=13, verbose_name='National Id')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15, verbose_name='Phone Number')),
                ('image', models.ImageField(upload_to='media/images/lecturer_profiles')),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('rollnumber', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Rollnumber')),
                ('school', models.CharField(max_length=30, verbose_name='School')),
                ('department', models.CharField(max_length=30, verbose_name='Department')),
                ('firstname', models.CharField(max_length=50, verbose_name='First Name')),
                ('lastname', models.CharField(max_length=50, verbose_name='Last Name')),
                ('idnumber', models.CharField(max_length=13, verbose_name='National Id')),
                ('currentclass', models.CharField(max_length=15, verbose_name='Class')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15, verbose_name='Phone Number')),
                ('image', models.ImageField(upload_to='media/images/student_profiles')),
            ],
        ),
        migrations.CreateModel(
            name='student_attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('course', models.CharField(max_length=30, verbose_name='Course')),
                ('arrivaltime', models.DateTimeField(auto_now_add=True, verbose_name='Time')),
                ('session', models.CharField(max_length=10, verbose_name='Session')),
                ('rollnumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.student')),
            ],
        ),
    ]
