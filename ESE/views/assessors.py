from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from ..decorators import assessor_required
from ESE.models import Student, Assessor, Assignment, Feedback, Competency, Module, Student_comp, User, Profile
from ESE.forms import StudentForm, StudentSignUpForm, ModuleForm, AssignmentForm, AssessorForm, AssessorSignUpForm, FeedbackForm, CompetencyForm,Student_compForm, ContactForm, ProfileForm


class AssessorSignUpView(CreateView):
    model = User
    form_class = AssessorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'assessor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
        #return redirect('teachers:quiz_change_list')

def assessor_dashboard(request):
    response = render (request, 'ESE/assessors/assessor_dashboard.html')
    return response

@method_decorator([login_required, assessor_required], name='dispatch')
def add_feedback(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
            messages.success(self.request, 'The feedback was created with success!')
            return render (request,'home.html')
        else:
            print(form.errors)
    return render(request, 'ESE/add_feedback.html', {'form': form})

@method_decorator([login_required, assessor_required], name='dispatch')
def add_competency(request):
    form = CompetencyForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
            messages.success(self.request, 'The new competency was created with success!')
            return render (request,'home.html')
        else:
            print(form.errors)
    return render(request, 'ESE/add_competency.html', {'form': form})