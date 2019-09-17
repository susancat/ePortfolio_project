from django.contrib import admin
from .models import Upload, Student, New, State, Rating, Module, Competency

class UploadAdmin(admin.ModelAdmin):
    list_display = ('name', 'competency', 'file')

class RatingAdmin(admin.ModelAdmin):
    list_display = ('student', 'competency', 'rating', 'feedback')

class RegisteredModuleAdmin(admin.ModelAdmin):
	list_display = ('user', 'module', 'competency', 'registered', 'featured', )


# admin.site.register(RegisteredCourse, RegisteredCourseAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(New)
admin.site.register(Student)
admin.site.register(Competency)
admin.site.register(Module)
admin.site.register(Upload, UploadAdmin)
admin.site.register(State)