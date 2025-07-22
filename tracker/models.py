from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CurrentBalance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    current_balance = models.FloatField(default=0.0)

    def __str__(self):
        return f"Current Balance: {self.current_balance}"

class TrackingHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null =True)
    current_balance = models.ForeignKey(CurrentBalance, on_delete=models.CASCADE, editable=False)
    amount = models.FloatField()
    expense_type = models.CharField(choices=(('CREDIT', 'Credit'), ('DEBIT', 'Debit')), max_length=6)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.expense_type} - {self.amount} - {self.description}"
    

class RequestLogs(models.Model):
    request_info = models.TextField()
    request_type = models.CharField(max_length = 100)
    request_method = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)


