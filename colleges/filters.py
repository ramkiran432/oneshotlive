import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class CollegeFilter(django_filters.FilterSet):


	class Meta:
		model = College
		fields = '__all__'
		exclude =['no_of_students']


class StudentFilter(django_filters.FilterSet):


	class Meta:
		model = Student
		fields = '__all__'
