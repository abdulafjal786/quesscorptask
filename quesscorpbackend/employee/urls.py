# employees/urls.py
from django.urls import path
from .views import AttendanceListView, EmployeeListView, EmployeeCreateView, EmployeeDeleteView, EmployeeSearchView, MarkAttendanceView

urlpatterns = [
    path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path('employees/add/', EmployeeCreateView.as_view(), name='employee-add'),
    path('employees/search/', EmployeeSearchView.as_view(), name='employee-add'),
    path('employees/delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee-delete'),
    path('attendance/', AttendanceListView.as_view(), name='attendance-list'),
    path('attendance/mark/', MarkAttendanceView.as_view(), name='attendance-mark'),
]
