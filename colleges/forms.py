from django.forms import ModelForm

from django import forms

from .models import *

class CollegeForm(ModelForm):
	class Meta:
		model = College
		fields = '__all__'
		

class StudentForm(ModelForm):
	class Meta:
		model = Student
		fields = '__all__'

