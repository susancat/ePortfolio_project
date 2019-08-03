from django.contrib import admin
from ESE.models import Student, Assessor, Assignment, Feedback, Competency, Module, Student_comp, User, Profile

class StudentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('SID',)}
    list_display = ('surname', 'first_name', 'SID', 'major', 'enroll_year', 'graduate_year' )

class AssessorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('assessor_ID',)}
    list_display = ('surname', 'first_name', 'assessor_ID', 'user_group', 'institution' )

class AssignmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('assignment_ID',), 'student_slug': ('SID',)} 
    list_display = ('title', 'assignment_ID', 'SID', 'assessor_ID', 'description')

class FeedbackAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('feedback_ID',), 'assignment_slug': ('assignment_ID',),'assessor_slug': ('assessor_ID',)}
    list_display = ('feedback_ID', 'assessor_ID', 'review_text')

class ModuleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('module_ID', 'name', 'SID')

class CompetencyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('group_name','dimension_name', 'name', 'description')

class StudentcompAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), 'student_slug': ('SID',)} 
    list_display = ('name','SID','semester','rating')

admin.site.register(Student, StudentAdmin)
admin.site.register(Assessor, AssessorAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Competency,CompetencyAdmin)
admin.site.register(Student_comp, StudentcompAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Profile)