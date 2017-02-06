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
        expense_op = ExpenseOperation(id, description=descriptionIn, expense=account, balance=balanceIn,
                                      operation_date=datetime.datetime.now())
        expense_op.save()

    expenses = Expense.objects.all()
    expenseOperations = ExpenseOperation.objects.all()
    current_date = datetime.datetime.now()
    return render_to_response('expense_operation.html',
                              {'accounts': expenses, 'now': current_date, 'expenseOperations':expenseOperations})

login_required
def expense(request):
    id = str(uuid4())
    nameIn = request.GET.get('name', '')

    if(not nameIn == ""):
        expense  = Expense(id, name = nameIn)
        expense.save()

    expenses = Expense.objects.all()
    return render_to_response('expense.html',
                              {'expenses': expenses})
# </Expense>

login_required
def index(request):
    return render(request, 'index.html')
