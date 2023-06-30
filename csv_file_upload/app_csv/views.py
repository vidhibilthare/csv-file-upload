from django.shortcuts import render
import io
import csv
from .models import Employee
# Create your views here.

def insert_data(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        decoded_file = csv_file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        next(io_string) 
        for row in csv.reader(io_string, delimiter=','):
            year_experience = float(row[0])
            salary = float(row[1])
            Employee.objects.create(
                year_experience = year_experience,
                salary = salary
            )
        return render(request,'success.html')
    return render(request,'insert.html')
     
def Employee_detail(request):
    search_query = request.GET.get('search')
    if search_query:
        employees = Employee.objects.filter(year_experience=search_query)
    else:
        employees = Employee.objects.all()
    return render(request, 'employee.html', {'employees': employees})