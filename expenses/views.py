from django.shortcuts import render,redirect

from .models import *

def home(request):
    profile = Profile.objects.filter(user=request.user).first() 
    expenses = Expenses.objects.filter(user = request.user)
    if request.method=="POST":

        name = request.POST.get('text')

        amount = request.POST.get('amount')

        expense_type = request.POST.get('type')
        expense = Expenses(name=name, amount=amount, expense_type=expense_type, user=request.user)
        expense.save()

        if expense_type =="Postive":
            profile.balance += float(amount)

        else:
            profile.expenses += float(amount)
            profile.balance -= float(amount)

        profile.save()
        return redirect('/')


        
    context = {'profile':profile,'expenses':expenses} 
    return render(request, 'project/home.html', context)