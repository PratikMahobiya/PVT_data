from django import forms
from emp.models import emp_table

class emp_form(forms.ModelForm):
	class Meta:
		model= emp_table
		fields= "__all__"