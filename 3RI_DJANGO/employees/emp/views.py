from django.shortcuts import render
from emp.form import emp_form

# Create your views here.
def index(request):
	e = emp_form()
	return render(request,'index.html',{'form':e})

def home(request):
	return render(request,'home.html')