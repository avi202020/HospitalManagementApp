# Generated by Django 2.2.6 on 2019-11-04 18:13

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
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone_number', models.PositiveIntegerField()),
                ('Address', models.CharField(max_length=250)),
                ('Message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Staff_strength', models.PositiveIntegerField()),
                ('Head_of_department', models.CharField(max_length=100)),
                ('Income_generated', models.PositiveIntegerField(blank=True, null=True)),
                ('Expenses', models.PositiveIntegerField(blank=True, null=True)),
                ('Duration', models.CharField(choices=[('JANUARY_JUNE', 'january_june'), ('JULY_DECEMBER', 'july_december')], max_length=50)),
                ('Function', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=100)),
                ('Last_name', models.CharField(max_length=100)),
                ('Phone_number', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('Reference', models.CharField(max_length=11)),
                ('Reference_phone_number', models.PositiveIntegerField()),
                ('Home_address', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=100)),
                ('Age', models.PositiveIntegerField(blank=True, null=True)),
                ('Country', models.CharField(max_length=100)),
                ('Position', models.CharField(max_length=100)),
                ('Salary', models.PositiveIntegerField(blank=True, null=True)),
                ('On_probation', models.BooleanField(default=True)),
                ('Number_of_queries', models.PositiveIntegerField(blank=True, null=True)),
                ('Joined', models.DateField()),
                ('Resigned', models.DateField(blank=True, null=True)),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Dashboard.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Salary', models.PositiveIntegerField()),
                ('Position', models.CharField(max_length=100)),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Dashboard.Department')),
                ('Name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Dashboard.Staff')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Request_by', models.CharField(max_length=100)),
                ('Position', models.CharField(max_length=100)),
                ('Amount', models.PositiveIntegerField()),
                ('Reason', models.CharField(max_length=250)),
                ('Approved', models.BooleanField(default=False)),
                ('Date', models.DateField()),
                ('Approved_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.Department')),
            ],
        ),
    ]
