from .models import Expense,ExpenseOperation
from uuid import uuid4
from django.shortcuts import render
import datetime
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required


login_required
def expense_operation(request):
    id = str(uuid4())
    descriptionIn = request.GET.get('inputDescription', '')

    if(not descriptionIn == ""):
        balanceIn = float(request.GET.get('inputBalance', 0))

        account = Expense.objects.get(id=request.GET.get('inputAccount', ''))
        expense_op = ExpenseOperation(id, description=account.name, expense=account, balance=balanceIn,
                                      operation_date=datetime.datetime.now())
        expense_op.save()

    expenses = Expense.objects.all()
    current_date = datetime.datetime.now()
    return render_to_response('expense_operation.html', {'accounts': expenses, 'now': current_date})

# </Expense>

def expense(request):
    return render(request, 'myapp/index.html')
