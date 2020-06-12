from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee
from .forms import userform
from django.contrib.auth.models import User
from django.http import *
from django.contrib import auth, messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.sessions.models import Session

# Create your views here.
def CreateEmp_View(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                return redirect(show_view)
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,'CURDApp/Create.html',{'form':form})


def show_view(request):
    if request.session.has_key('is_logged'):
        employee=Employee.objects.all()
        return  render(request,'CURDApp/Show.html',{'empData':employee})

    return redirect(login_view)



def delete_Emp_view(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect(show_view)

def update_Emp_view(request,id):
    print('in view')
    employee = Employee.objects.get(id=id)
    print('in view',employee)

    form = EmployeeForm(request.POST, instance=employee)
    print('in view', form)
    print(form.is_valid())
    if form.is_valid():

        print('in if')
        form.save()
        return redirect(show_view)

    return render(request,'CURDApp/Update.html',{'empdata':employee})


def edit_Emp_view(request,id):
    employee = Employee.objects.get(id=id)
    return render(request, 'CURDApp/Update.html', {'empdata': employee})

def login_view(request):
    if request.session.has_key('is_logged'):
        return redirect(show_view)
    if request.method == "POST":
        username = request.POST['user']
        password = request.POST['pas']
        try:
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                request.session['is_logged']=True
                return redirect(show_view)
            else:
                messages.error(request,"Username and Password did not match.")
        except auth.ObjectDoesNotExist:
            print("invalid user")
    return  render(request,'CURDApp/Login.html')

def logout_view(request):
    auth.logout(request)
    return render(request, 'CURDApp/Login.html')



'''def login_view(request):
    if request.method == "POST":
        form = UsersForm(request.POST)
        print(form)
        if form.is_valid():
            user = Users.objects.get(username=request.POST['username'])
            print(user)
            # print(user.password)
            print(request.POST['password'])
            # if user.password == request.POST['password']:
            #     request.session['member_id'] = user.id
            #     return redirect(show_view)
            # else:
            msg = "Your username and password didn't match."
            return render(request, 'CURDApp/login.html', {'msg': msg})

    else:
        form = UsersForm()
        return render(request,'CURDApp/Login.html',{'form':form})
'''

def registration_view(request):
    if request.method == "POST":
        form1 = userform(request.POST)
        if form1.is_valid():
            username = form1.cleaned_data['username']
            first_name = form1.cleaned_data['first_name']
            last_name = form1.cleaned_data['last_name']
            email = form1.cleaned_data['email']
            password = form1.cleaned_data['password']
            User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            return HttpResponseRedirect('/registration/')
    else:
        form1=userform()
        return render(request,'CURDApp/Registration.html',{'form1':form1})