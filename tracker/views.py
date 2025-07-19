from django.shortcuts import render , redirect
from .models import TrackingHistory, CurrentBalance
from django.contrib import messages
# Create your views here.

def index(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        current_balance, _ = CurrentBalance.objects.get_or_create(id = 1)
         if amount == '' or float(amount) == 0:
            messages.error(request, "Amount cannot be zero or empty")
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

def delete_transaction(request, id):
    tracking_history = TrackingHistory.objects.filter(id = id)
    if tracking_history.exists():
            current_balance, _ = CurrentBalance.objects.get_or_create(id = 1)
            tracking_history = tracking_history.first()
            current_balance.current_balance -= tracking_history.amount
            current_balance.save()
    tracking_history.delete()
    return redirect('/')
