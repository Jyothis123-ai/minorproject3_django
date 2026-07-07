from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import employee
from .serializers import EmployeeSerializer
@api_view(['GET'])
def view_employee(request):
    
    employees = employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)
@api_view(['POST'])
def add_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Employee added successfully", "employee": serializer.data})
    return Response(serializer.errors)
@api_view(['PUT'])
def update_employee(request, id):
    employee_instance = employee.objects.get(id=id)
    serializer = EmployeeSerializer(employee_instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Employee updated successfully", "employee": serializer.data})
    return Response(serializer.errors)
@api_view(['DELETE'])
def delete_employee(request, id):
    employee_instance = employee.objects.get(id=id)
    employee_instance.delete()
    return Response({"message": "Employee deleted successfully"})

# Create your views here.
