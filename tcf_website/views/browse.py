from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout, login
from django.http import JsonResponse
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder

from ..models import School, Department

def browse(request):
    schools = School.objects.all()
    return render(request, 'browse/browse.html', {'schools': schools})

def department(request, dept_id):
    dept = Department.objects.get(pk=dept_id)
    subdepartments = dept.subdepartment_set.all()
    return render(request, 'department/department.html', {'department': dept, 'subdepartments': subdepartments})