from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView
from ESE.models import Student, Assessor, Assignment, Feedback, Competency, Module, Student_comp, User, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from registration.backends.simple.views import RegistrationView
from ESE.forms import StudentForm, StudentSignUpForm, ModuleForm, AssignmentForm, AssessorForm, AssessorSignUpForm, FeedbackForm, CompetencyForm,Student_compForm, ContactForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from django.core.mail import send_mail

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

def base(request):
    #competency_list = Competency.objects.all()
    #context_dict = {'competency': competency_list}
    response = render (request, 'ESE/base.html')
     #, context_dict')
    return response

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.info(request,'Your ESE account is disabled.')
                return HttpResponseRedirect(reverse('signin'))
        else:
            messages.error(request,'Invalid login details supplied. Please check your username and password!')
        return HttpResponseRedirect(reverse('signin'))

    else:
        return render(request, 'ESE/registration/login.html', {})

def home(request):
    if request.user.is_authenticated:
        if request.user.is_assessor:
            return redirect('home')
        else:
            #return redirect('students:assignment_list')
            return redirect('about')
    return render(request, 'ESE/home.html')

def about(request):
    return render(request, 'ESE/about.html', {})

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['enquiry@exampleco.com'])
            messages.info(request,'Thanks for  contacting us!')
            return HttpResponseRedirect(reverse('contact_us'))
    else:
        form = ContactForm()

    return render(request, 'ESE/contact_us.html', {'form': form})


'''
@login_required
def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def sign_up(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                profile.save()
            registered = True
            messages.success(request, 'You have sign up successfully!')  

        else:
            messages.error(request,'User already exists, enter new details')
            print(user_form.errors, profile_form.errors)


    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request,
                  'ESE/sign_up.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered
                  })

@login_required
def register_profile(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            
            return redirect('home')
        else:
            print(form.errors)

    context_dict = {'form':form}
    
    return render(request, 'ESE/profile_registration.html', context_dict)

def some_view(request):
    if not request.user.is_authenticated():
        return HttpResponse("You are logged in.")
    else:
        return HttpResponse("You are not logged in.")
'''
@login_required
def my_account(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('home')
    
    profile = Profile.objects.get_or_create(user=user)[0]
    form = ProfileForm({'picture': profile.picture})
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('my_account', user.username)
        else:
            print(form.errors)
    
    return render(request, 'ESE/my_account.html', {'profile': profile, 'selecteduser': user, 'form': form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def show_student (request, student_surname_slug):
    
    context_dict = {}

    try:
        student = Student.objects.get(slug = student_surname_slug)
        student_comp = Student_comp.objects.filter(student = student)
        context_dict['student_comps'] = student_comp
        context_dict['student'] = student
    
    except Student.DoesNotExist:
        context_dict['student'] = None
        context_dict['student_comps'] = None

    return render(request, 'ESE/show_student.html', context_dict)

@login_required
def show_assessor (request, assessor_surname_slug):
    context_dict = {}

    try:
        assessor = Assessor.objects.get(slug = assessor_surname_slug)
        context_dict['assessor'] = assessor
    
    except Assessor.DoesNotExist:
        context_dict['assessor'] = None
        
    return render(request, 'ESE/show_assessor.html', context_dict)


def show_competency (request, competency_ID_slug):
    context_dict = {}

    try:
        competency = Competency.objects.get(slug = competency_ID_slug)
        context_dict['competency'] = competency
    
    except Competency.DoesNotExist:
        context_dict['competency'] = None
        
    return render(request, 'ESE/show_competency.html', context_dict)

@login_required
def show_studentcomp(request, student_surname_slug, student_comp_name_slug): 
    context_dict = {}

    try:
        student_comp = Student_comp.objects.filter(slug = student_comp_name_slug)
        context_dict['student_comp'] = student_comp
    
    except Student_comp.DoesNotExist:
        context_dict['student_comp'] = None

    return render(request, 'ESE/show_studentcomp.html', context_dict)

@login_required
def show_assignment (request, assignment_ID_slug):
    context_dict = {}

    try:
        assignment = Assignment.objects.get(slug = assignment_ID_slug)
        feedback = Feedback.objects.filter(assignment = assignment)
        context_dict['feedback'] = feedback
        context_dict['assignment'] = assignment
    
    except Assignment.DoesNotExist:
        context_dict['assignment'] = None
        context_dict['feedback'] = None

    return render(request, 'ESE/show_assignment.html', context_dict)

'''
@method_decorator([login_required], name='dispatch')
class StudentInterestsView(UpdateView):
    model = Student
    form_class = StudentInterestsForm
    template_name = 'classroom/students/interests_form.html'
    success_url = reverse_lazy('students:quiz_list')

    def get_object(self):
        return self.request.user.student

    def form_valid(self, form):
        messages.success(self.request, 'Interests updated with success!')
        return super().form_valid(form)
'''
def show_feedback (request, assignment_ID_slug, feedback_ID_slug):
    context_dict = {}

    try:
        feedback = Feedback.objects.filter(slug = feedback_ID_slug)
        context_dict['feedback'] = feedback
    
    except Feedback.DoesNotExist:
        context_dict['feedback'] = None

    return render(request, 'ESE/feedback.html', context_dict)