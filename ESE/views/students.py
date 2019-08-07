from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from ..decorators import student_required
from ESE.models import Student, Assessor, Assignment, Feedback, Competency, Module, Student_comp, User, Profile
from ESE.forms import StudentForm, StudentSignUpForm, ModuleForm, AssignmentForm, AssessorForm, AssessorSignUpForm, FeedbackForm, CompetencyForm,Student_compForm, ContactForm, ProfileForm


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

def student_dashboard(request):
    response = render (request, 'ESE/students/student_dashboard.html')
    return response


@login_required
@student_required
def add_assignment(request):
    form = AssignmentForm()
    if request.method == 'POST':
        form = AssignmentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
            messages.success(self.request, 'The new assignment was created with success!')
            return render (request,'home.html')
        else:
            print(form.errors)
    return render(request, 'ESE/students/add_assignment.html', {'form': form})