# employees/serializers.py
from rest_framework import serializers
from .models import Attendance, Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'employee_id', 'full_name', 'email', 'department']
        
class AttendanceSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='employee.full_name', read_only=True)
    class Meta:
        model = Attendance
        fields = ['id', 'employee_name','employee', 'date', 'status']