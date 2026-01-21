# employees/views.py
from django.forms import ValidationError
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Attendance, Employee
from .serializers import AttendanceSerializer, EmployeeSerializer
from rest_framework.generics import ListAPIView

from rest_framework.filters import SearchFilter

# View all employees
class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Add a new employee
class EmployeeCreateView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Delete an employee
class EmployeeDeleteView(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    
    
    
class AttendanceListView(generics.ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

# Mark attendance (create or update)
class MarkAttendanceView(generics.CreateAPIView):
    serializer_class = AttendanceSerializer

    def create(self, request, *args, **kwargs):
        employee_id = request.data.get('employee')
        date = request.data.get('date', timezone.now().date())
        status_value = request.data.get('status')

        if not employee_id or not status_value:
            return Response(
                {"error": "Employee and status are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Normalize status
        status_value = status_value.lower()

        if status_value not in ['present', 'absent']:
            return Response(
                {"error": "Status must be 'present' or 'absent'"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Try to get the employee
            employee = Employee.objects.get(id=employee_id)
        except Employee.DoesNotExist:
            # Maybe the ID is the employee_id field, not the primary key
            try:
                employee = Employee.objects.get(employee_id=employee_id)
                # Use the primary key for the foreign key
                employee_id = employee.id
            except Employee.DoesNotExist:
                return Response(
                    {"error": f"Employee with ID '{employee_id}' not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

        # Now create or update the attendance
        try:
            attendance, created = Attendance.objects.update_or_create(
                employee_id=employee_id,
                date=date,
                defaults={'status': status_value}
            )

            serializer = self.get_serializer(attendance)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED if created else status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class EmployeeSearchView(ListAPIView):
    serializer_class = EmployeeSerializer
    filter_backends = [SearchFilter]
    search_fields = ['full_name', 'employee_id', 'email']

    def get_queryset(self):
        search = self.request.query_params.get('search')

        if not search:
            raise ValidationError({
                "search": "Search parameter is required."
            })

        return Employee.objects.all()