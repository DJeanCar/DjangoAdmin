from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    def get_changeform_initial_data(self, request):
        return {'teacher': request.user.id}