from django.contrib import admin
from .models import Attendance,StudentExtra,TeacherExtra,Notice,StaffLeave
# Register models 
class StudentExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentExtra, StudentExtraAdmin)

class TeacherExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(TeacherExtra, TeacherExtraAdmin)

class AttendanceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Attendance, AttendanceAdmin)

class NoticeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Notice, NoticeAdmin)

class StaffLeaveAdmin(admin.ModelAdmin):
    pass
admin.site.register(StaffLeave, StaffLeaveAdmin)