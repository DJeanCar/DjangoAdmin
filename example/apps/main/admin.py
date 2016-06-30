from django.contrib import admin
from django import forms
from .models import Course
# Register your models here.
class FooAdminForm(forms.ModelForm):

  class Meta:
      model = Course
      fields = "__all__"

  def __init__(self, *args, **kwargs):
    dic = {'teacher': 2}
    teacher_id = kwargs['initial'].get('teacher')
    # print teacher_id
    dic2 = dict(kwargs['initial'])
    if teacher_id:
        kwargs['initial'].update({'teacher': teacher_id})
    super(FooAdminForm, self).__init__(*args, **kwargs)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    """def get_form(self, request, *args, **kwargs):
        print request.user
        form = FooAdminForm(**{"initial":{"teacher": request.user.id}})
        return FooAdminForm
"""
    def get_changeform_initial_data(self, request):
        return {'teacher': request.user.id}