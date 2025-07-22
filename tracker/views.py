from django.shortcuts import render , redirect
from .models import TrackingHistory, CurrentBalance
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username = username)
        if not user.exists():
            messages.success(request, "Username not found") 
            return redirect('/login/')
        
        user = authenticate(username = username , password = password)
        if not user:
            messages.error(request, "Incorrect password") 
            return redirect('/login/')
        
        login(request , user)
        return redirect('/')

    return render(request , 'login.html')


def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.error(request, "Username is already taken") 
            return redirect('/register/')
        
        user = User.objects.create_user(
            username = username,
            first_name = first_name,
            last_name = last_name,
            password = password
        )
        user.save()
        messages.success(request, "Account created") 
        return redirect('/login/')
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required(login_url="login_view2") # requires login to access the index view

def index(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        current_balance, _ = CurrentBalance.objects.get_or_create(id = 1)
        if amount == '' or float(amount) == 0:
            messages.error(request, "Amount cannot be zero or empty.")
            return redirect('/')
        if float(amount) < 0:
            expense_type = 'DEBIT'
        else:
            expense_type = 'CREDIT'
       
        tracking_history = TrackingHistory.objects.create(
            current_balance=current_balance,
            amount=amount,
            expense_type=expense_type,
            description=description
        )
        current_balance.current_balance += float(tracking_history.amount)
        current_balance.save()
        # print(f"Description: {description}, Amount: {amount}") # Debugging line to check form data coming or not
        return redirect('/')
    income = 0
    expense = 0
    for transaction in TrackingHistory.objects.all():
        if transaction.expense_type == 'CREDIT':
            income += transaction.amount
        else:
            expense += transaction.amount
    current_balance, _ = CurrentBalance.objects.get_or_create(id = 1)
    context = {'transactions': TrackingHistory.objects.all(),
               'current_balance' : current_balance,
               'income': income,
               'expense': expense
               }
    return render(request, 'index.html', context)

@login_required(login_url="login_view2") # requires login to access the delete_transaction view

def delete_transaction(request, id):
    tracking_history = TrackingHistory.objects.filter(id = id)
    if tracking_history.exists():
            current_balance, _ = CurrentBalance.objects.get_or_create(id = 1)
            tracking_history = tracking_history.first()
            current_balance.current_balance -= tracking_history.amount
            current_balance.save()
    tracking_history.delete()
    return redirect('/')