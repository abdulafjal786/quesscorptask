from django.contrib import admin
from .models import Employee, Attendance

# Employee admin
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee_id', 'full_name', 'email', 'department')
    search_fields = ('full_name', 'email', 'department', 'employee_id')
    list_filter = ('department',)
    ordering = ('id',)

# Attendance admin
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'date', 'status')
    list_filter = ('status', 'date')
    search_fields = ('employee__full_name', 'employee__employee_id')

# Register models
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Attendance, AttendanceAdmin)
