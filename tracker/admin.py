from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "Expense Tracker Admin"
admin.site.site_title = "Expense Tracker Admin Portal"
# admin.site.site_url = "Expense Tracker"

# admin.site.disable_action("delete_selected") # Disable the delete selected action


@admin.action(description="Mark selected expenses as CREATED")
def make_credit(modeladmin, request, queryset):
    for item in queryset:
        if item.amount:
            item.amount = -item.amount
        item.save()  # Save the updated item
    queryset.update(expense_type="CREDIT")


    
@admin.action(description="Mark selected expenses as DEBITED")
def make_debit(modeladmin, request, queryset):
    for item in queryset:
        if item.amount:
            item.amount = -item.amount
        item.save()  # Save the updated item
    queryset.update(expense_type="DEBITED")


class TrackingHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'current_balance',
                    'description',
                    'amount',
                    'expense_type',
                    'created_at',
                    'type')
    search_fields = ('description','expense_type')
    ordering = ['-created_at'] # descending order
    list_filter = ['expense_type']

    actions = [make_credit, make_debit]

    def type(self, obj):
        return "Positive" if obj.expense_type == "CREDIT" else "Negative"

admin.site.register(CurrentBalance)
admin.site.register(TrackingHistory, TrackingHistoryAdmin)
# admin.site.register(RequestLogs)