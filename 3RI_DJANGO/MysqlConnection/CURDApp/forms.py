from django import forms
from CURDApp.models import Employee
#from CURDApp.models import Users
from django.contrib.auth.models import User

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
       # fields = ('empid','ename')
        fields = "__all__"

'''class UsersForm(forms.ModelForm):
    class Meta:
        model=Users
        fields = "__all__"
        '''

class userform(forms.ModelForm):
    '''username = forms.CharField(widget=forms.TextInput(attrs = {'placeholder':'Enter user name'}),required=True, max_length=50)
    email = forms.CharField(widget=forms.EmailField(attrs={'placeholder':'Enter user name'}), required=True, max_length=50)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter user name'}), required=True,max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter user name'}), required=True,max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter user name'}), required=True,max_length=50)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter user name'}), required=True,max_length=50)
'''
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter user name'}),
                               max_length=50)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Enter user name'}),
                            max_length=50)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter user name'}),
                                 max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter user name'}),
                                max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter user name'}),
                               max_length=50)
    confirm_password = forms.CharField(widget=forms.PasswordInput()
                                       , max_length=50)
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password']


