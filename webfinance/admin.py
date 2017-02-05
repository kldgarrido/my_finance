from django.contrib import admin

from .models import Expense #Ingress, IngressOperation, Expense, ExpenseOperation

#admin.site.register(Ingress)
#admin.site.register(IngressOperation)
admin.site.register(Expense)
#admin.site.register(ExpenseOperation)