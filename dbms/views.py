from django.shortcuts import render, redirect
from .models import employee
from .forms import employeeForm
from .models import members
from .forms import memberForm
#admin sucess
def adminsucess(request):
    return render(request, 'adminsucess.html')
#employee views
def employee_list(request):
    employees = employee.objects.all()
    form = employeeForm()

    if request.method == 'POST':
        form = employeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')

    return render(request, 'employee_list.html', {'employees': employees, 'form': form})

def delete_employee(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_ids')
        employee.objects.filter(id__in=selected_ids).delete()
        return redirect('employee_list')

def update_employee(request, employee_id):
    employee = employee.objects.get(id=employee_id)
    if request.method == 'POST':
        form = employeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = employeeForm(instance=employee)

    return render(request, 'update_employee.html', {'form': form, 'employee_id': employee_id})

#member views
def members_list(request):
    member = members.objects.all()
    form = memberForm()

    if request.method == 'POST':
        form = memberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('members_list')

    return render(request, 'members_list.html', {'member': member, 'form': form})

def delete_members(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_ids')
        members.objects.filter(id__in=selected_ids).delete()
        return redirect('members_list')

def update_members(request, members_id):
    memberr = members.objects.get(id=members_id)
    if request.method == 'POST':
        form = memberForm(request.POST, instance=memberr)
        if form.is_valid():
            form.save()
            return redirect('members_list')
    else:
        form = memberForm(instance=memberr)

    return render(request, 'update_members.html', {'form': form, 'members_id': members_id})

