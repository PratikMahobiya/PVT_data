from django.shortcuts import render,redirect
from django.http import HttpResponse
from crudapp.form import EmployeeForm
from crudapp.models import Employee

# Create your views here.

def createemp(request):
	if request.method == "POST":
		form = EmployeeForm(request.POST)
		if form.is_valid():
			eid= request.POST.get('eid','')
			ename= request.POST.get('ename','')
			eemail= request.POST.get('eemail','')
			econtact= request.POST.get('econtact','')
			emp_obj = Employee(eid=eid , ename=ename , eemail=eemail , econtact=econtact)
			emp_obj.save()
			return redirect('/display')
		else:
			form = EmployeeForm()
	return render(request, 'index.html',{'form': Employee})

def display(request):
	e = Employee.objects.all()
	return render(request,'display.html',{'e': e})
