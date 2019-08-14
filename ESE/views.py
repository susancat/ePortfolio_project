from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import redirect
from ESE.models import Module, Competency, User, Upload, Student, New, Rating
from django.contrib.auth.models import User, Group
from ePortfolio_project import settings
from django.db.models import Sum, Avg, Max, Min, Count
from ESE.forms import UploadFormFile, UpdateProfile, SelectAssessorsForm, AddPostForm, RatingStudentsForm, ModuleForm, CompetencyAddForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from django.forms import inlineformset_factory
from django.forms import modelformset_factory
from django.core.paginator import Paginator
from django import forms
from django.template.defaulttags import register


max_paraqit = 3

@register.filter
def toInt(value):
    return int(value)

@register.filter
def toStr(value):
    return str(value)

@register.filter
def addOne(value):
    value = value + 1
    return value

@register.filter
def get_rating(course, user):
    rating = list(Rating.objects.values_list('rating', flat=True).filter(module__pk=module, student__pk=user))
    if not rating:
        return 0
    return rating[0]

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def sub(value, arg):
    return value - arg
# ########################################################

def modules_view(request):
    modules = Module.objects.all()

    if request.user.is_authenticated:
        return render (
            request,
            'modules_list.html',
            {'modules': modules},
        )
    else:
        return redirect('login')


def module_add(request):
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('modules')
    else:
        form = ModuleForm()

    return render (
        request, 'module_add.html', {'form': form},
    )


def module_delete(request, pk):
    module = Module.objects.get(pk=pk)
    module.delete()

    return redirect('modules')


def module_edit(request, pk):
    module = Module.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = ModuleForm(request.POST, instance=module)
        if form.is_valid():
            form.save()
            return redirect('modules')
    else:
        form = ModuleForm(instance=module)

    return render(
        request, 'module_add.html', {'form': form},
    )


def module_detail(request, pk):
    module = Module.objects.get(pk=pk)
    competencies = Competency.objects.filter(id=pk)
    # credits = Course.objects.aggregate(Sum('credits'))

    paginator = Paginator(competencies, 10)
    page = request.GET.get('page')

    competencies = paginator.get_page(page)

    if request.user.is_authenticated:
        return render(
            request,
            'module_single.html',
            {'module': module, 'competencies': competencies},
        )# here used to be 'credits':credits, see later if we need to add rating here
    else: 
        return redirect('login')


# ########################################################

def students_view(request):
    students = Student.objects.all()
    modules = Module.objects.all()

    if request.method == 'GET':
        m = request.GET.get('module', '')
        name = request.GET.get('name', '')
        email = request.GET.get('email', '')

        if m != '':
            students = Student.objects.filter(module=m, first_name__contains=name, email__contains=email)
        else:
            students = Student.objects.filter(first_name__contains=name, email__contains=email)

    if request.user.is_authenticated:
        return render(
            request,
            'students_list.html',
            {'students': students, 'modules': modules, 'media_url': settings.MEDIA_ROOT},
        )
    else:
        return redirect('login')


def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    success = Rating.objects.filter(student=student.user).order_by('-rating')
    details = Rating.objects.filter(student=student.user, rating__gt=1).aggregate(Sum('rating'), Max('rating'), Min('rating'))

    if request.user.is_authenticated:
        return render(
            request, 'student_profile.html', {'student': student, 'success': success, 'details': details},
        )
    else:
        return redirect('login')


# ########################################################

def competency_detail(request, pk):
    competency = Competency.objects.get(pk = pk)
    files = Upload.objects.filter(competency_id = pk)
    users = User.objects.filter(student__assessor__in=[competency])
    ratings = Rating.objects.filter(student_id=request.user.id, competency_id=pk)
    assessors = Student.objects.filter(assessor__in=[competency])

    if request.user.is_authenticated:
        return render(
            request, 'competency_single.html', {'usrs': users, 'competency': competency, 'files': files, 'ratings': ratings, 'assessors': assessors, 'media_url': settings.MEDIA_ROOT},
        )
    else:
        return redirect('login')



def update_assessor(pk_t1):
    pk_t1 = int(pk_t1)
    if pk_t1 > 0:
        competency = Competency.objects.latest('pk')
        t1 = User.objects.get(pk=pk_t1)
# not sure if here should be module
        if not User.objects.filter(student__assessor__in=[competency], pk=pk_t1).exists():
            t1.student.assessor.add(competency)



def competency_add(request, pk):
    users = User.objects.all()
    if request.method == 'POST':
        form = CompetencyAddForm(request.POST)
        if form.is_valid():
            form.save()
            update_assessor(request.POST.get('user_1'))
            if request.POST.get('submit') != 'save':
                return redirect('competency_add', pk=pk)
            return redirect('module_detail', pk=request.POST.get('module'))
    else:
        form = CompetencyAddForm(initial={'module': Module.objects.get(pk=pk)})

    if request.user.is_authenticated and request.user.is_superuser:
        return render (
            request, 'competency_add.html', {'form': form, 'module': pk, 'users': users},
        )
    else:
        return redirect('login')


def competency_edit(request, pk):
    users = User.objects.all()
    competency = get_object_or_404(Competency, pk=pk)
    if request.method == 'POST':
        form = CompetencyAddForm(request.POST, instance=competency)
        if form.is_valid():
            form.save()
            return redirect('module_detail', pk=request.POST.get('module'))
    else:
        form = CompetencyAddForm(instance=competency)

    # print(form.errors)

    if request.user.is_authenticated and request.user.is_superuser:
        return render (
            request, 'competency_add.html', {'form': form, 'module': pk, 'users': users, 'competency': pk},
        )
    else:
        return redirect('login')


def competency_delete(request, pk, p_pk):
    competency = Competency.objects.get(pk=pk)
    competency.delete()

    return redirect('module_single', pk=p_pk)


# ########################################################

def handle_file_upload(request, competency_id):
    competency = Competency.objects.get(pk = competency_id)
    if request.method == 'POST':
        form = UploadFormFile(request.POST, request.FILES, {'competency': competency})
        if form.is_valid():
            form.save()
            return redirect('/modules/competency/' + str(competency_id))
    else:
        form = UploadFormFile()
    return render(
        request, 'upload_file_form.html', {'form': form, 'competency': competency},
    )


def handle_file_edit(request, competency_id, file_id):
    competency = Competency.objects.get(pk=competency_id)
    instance = Upload.objects.get(pk=file_id)
    if request.method == 'POST':
        form = UploadFormFile(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('competency_detail', pk=competency_id)
    else:
        form = UploadFormFile(instance=instance)

    return render (
        request, 'upload_file_form.html', {'form': form, 'competency': competency}
    )


def handle_file_delete(request, competency_id, file_id):
    file = Upload.objects.get(pk=file_id)
    file.delete()

    return redirect('competency_detail', pk=competency_id)


# ########################################################

def user_add(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            uid = Student.objects.latest('pk').pk
            return redirect('user_edit', pk=uid)
    else:
        form = UserCreationForm()

    print(form.errors)

    if request.user.is_authenticated and request.user.is_superuser:
        return render(
            request, 'user_add.html', {'form': form},
        )
    else:
        return redirect('login')


def user_delete(request, pk):
    usr = get_object_or_404(User, pk=pk)
    usr.delete()

    return redirect('students')


def user_edit(request, pk):
    student = Student.objects.get(pk=pk)

    instance = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = UpdateProfile(request.POST, request.FILES, instance = instance)
        if form.is_valid():
            form.save(commit=False)

            competencies = request.POST.getlist('competency')
#display module and then competency
            is_super = request.POST.get('is_super')

            if is_super:
                usr = User.objects.get(pk=student.user.pk)
                usr.is_admin = True
                usr.is_staff = True
                usr.is_superuser = True
                usr.save()

            for c in competencies:
                rating = Rating()
                usr = User.objects.get(pk=request.POST.get('user'))
                comp = Competency.objects.get(pk=c)
                if not Rating.objects.filter(competency=comp, student=usr).exists():
                    rating.student = usr
                    rating.rating = 0
                    rating.competency = comp
                    rating.save()
    
            existing_competencies = list(Student.objects.values_list('competency', flat=True).filter(pk=pk))
                
            for c in existing_competencies:
                if str(c) not in competencies:
                    Rating.objects.filter(student=User.objects.get(pk=request.POST.get('user')), competency=c).delete()

            form.save()
            return redirect('students')
    else:
        form = UpdateProfile(instance=instance, initial=({'is_super': User.objects.get(pk=student.user.pk).is_superuser}))

    return render(
        request, 'user_profile_edit.html', {'form': form, 'student': student},
    )

# ########################################################


def select_assessor(request, competency_id):
    students = Student.objects.all()
    curr_assessors = Student.objects.filter(assessor__in=[Competency.objects.get(pk=competency_id)])

    if request.method == 'GET':
        first_name = request.GET.get('first_name', '')
        last_name = request.GET.get('last_name', '')
        students = Student.objects.filter(first_name__contains=first_name, last_name__contains=last_name).exclude(assessor__in=[Competency.objects.get(pk=competency_id)])

    paginator = Paginator(students, 15)

    page = request.GET.get('page')
    students = paginator.get_page(page)

    return render (
        request, 'select_assessor.html', {'students': students, 'competency_id': competency_id, 'assessors': curr_assessors},
    )

# ########################################################


def confirm_select_assessor(request, competency_id, student_id):
    student = Student.objects.get(pk=student_id)
    competency = Competency.objects.get(pk=competency_id)

    student.assessor.add(competency)
    student.save()

    return redirect('add_assessor', competency_id=competency_id)    



def confirm_delete_assessor(request, competency_id, student_id):
    student = Student.objects.get(pk=student_id)
    competency = Competency.objects.get(pk=competency_id)

    student.assessor.remove(competency)
    student.save()

    return redirect('add_assessor',  competency_id=competency_id)

# ########################################################


# AJAX Call
def filter_competencies_view(request):
    module = request.GET.get('module', None)
    competency = Competency.objects.filter(module=module).values('pk', 'name' )
    data = list(competency)
    return JsonResponse(data, safe=False)

# ########################################################

def home_view(request):
    uploads = Upload.objects.all().order_by('-upload_time')[:5]
    modules = Module.objects.all()
    users = User.objects.all().order_by('-last_login')[:5]
    news = New.objects.all().order_by('-create_date')[:3]

    if request.user.is_authenticated:
        return render (
            request, 'home.html', {'uploads': uploads, 'modules': modules, 'users': users, 'news': news},
        )
    else:
        return redirect('login')

# ########################################################


def post_list(request):

    posts = New.objects.all().order_by('-create_date')
    paginator = Paginator(posts, 12)

    page = request.GET.get('page')
    post = paginator.get_page(page)

    return render(
        request, 'post_list.html', {'posts': post}, 
    )


def post_single(request, pk):
    post = New.objects.get(pk=pk)
    posts = New.objects.all().order_by('-create_date')[:5]
    uploads = Upload.objects.all().order_by('-upload_time')[:5]

    if request.user.is_authenticated:
        return render (
            request, 'post_single.html', {'post': post, 'posts': posts, 'uploads': uploads},
        )
    else:
        return redirect('login')


def post_add(request):

    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()

    if request.user.is_authenticated and request.user.is_superuser:
        return render (
            request, 'add_new_post.html', {'form': form},
        )
    else:
        return redirect('login')


def post_edit(request, pk):
    post = New.objects.get(pk=pk)

    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm(instance=post)

    if request.user.is_authenticated and request.user.is_superuser:
        return render (
            request, 'add_new_post.html', {'form': form},
        )
    else:
        return redirect('login')


def post_delete(request, pk):
    post = get_object_or_404(New, pk=pk)
    post.delete()

    return redirect('home')

# ########################################################


def rating_students(request, competency_id):
    competency = Competency.objects.get(pk=competency_id)
    curr_ratings = Rating.objects.filter(competency=competency)

    queryset = Rating.objects.filter(competency=competency)

    RatingStudentsFormSet = forms.modelformset_factory(Rating, form=RatingStudentsForm, extra=0)

    if request.method == 'POST':
        formset = RatingStudentsFormSet(request.POST, queryset=queryset)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.save()
            return redirect('competency_detail', pk=competency_id)
        else:
            print(formset.errors)
    else:
        formset = RatingStudentsFormSet(queryset=queryset)

    return render (
        request, 'rating_students.html', {'formset': formset, 'competency': competency},
    )

# ########################################################

'''
in user-edit
for m in modules:
    competency = Competency()
    usr = User.objects.get(pk=request.POST.get('user'))
    mod = Module.objects.get(pk=m)
    if not Competency.objects.filter(module=mod, student=usr).exists():
        competency.student = usr
        competency.competency = 0
        competency.module = mod
        competency.save()

existing_modules = list(Student.objects.values_list('module', flat=True).filter(pk=pk))
    
for m in existing_modules:
    if str(m) not in modules:
        Competency.objects.filter(student=User.objects.get(pk=request.POST.get('user')), module=m).delete()
                        

def year_add(request):

    if request.method == 'POST':
        form = LendetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('current_years')
    else:
        form = LendetForm()

    return render (
        request, 'year_add.html', {'form': form}, 
    )


def year_edit(request, pk):
    current = ProvimetMundshme.objects.get(pk=pk)
    courses = ProvimetMundshme.objects.values_list('course', flat=True).filter(pk=pk)

    if request.method == 'POST':
        form = LendetForm(request.POST, instance=current)
        if form.is_valid():
            form.save()
            return redirect('current_years')
    else:
        form = LendetForm(instance=current, initial={'course': list(courses)})

    return render (
        request, 'year_add.html', {'form': form}, 
    )


def register_courses(request):
    pass


def register_course(request, pk, max_reached):
    if not max_reached:
        regs = RegisteredCourse()
        regs.user = request.user
        regs.program = request.user.student.program
        regs.course = Course.objects.get(pk=pk)
        regs.registered = True
        regs.featured = False

        regs.save()

    return redirect('register_courses')



# ADMIN
def admin_view(request, afat_extra):

    if not afat_extra:
        afat_extra = 0

    queryset = afatet_provimeve.objects.all()
    AfatetFormSet = forms.modelformset_factory(afatet_provimeve, form=AfatetForm, extra=afat_extra)

    if request.method == 'POST':
        formset = AfatetFormSet(request.POST, queryset=queryset)
        if formset.is_valid():
            for instance in formset.forms:
                if instance.cleaned_data.get('emri'):
                    instance.save()
            return redirect('administrator', afat_extra=0)
        else: 
            print(formset.errors)
    else:
        formset = AfatetFormSet(queryset=queryset)

    return render (
        request, 'admin_panel.html', {'formset': formset, 'extra': afat_extra},
    )


def delete_afat(request, pk):
    afati = get_object_or_404(afatet_provimeve, pk=pk)
    afati.delete()

    return redirect('administrator', afat_extra=0)


def paraqit_provimet(request):
    provimetList = list()
    courses = None
    provimet = None
    afatet = afatet_provimeve.objects.filter(aktiv=True)
    afatetAll = afatet_provimeve.objects.all()
    program = request.user.student.program

    if request.method == 'GET':
        if request.GET.get('filter'):
            year = int(request.GET.get('year'))
            semester = int(request.GET.get('semester'))
            if int(request.GET.get('afati')) > -1:
                afati = get_object_or_404(afatet_provimeve, pk=int(request.GET.get('afati')))
                provimetList = list(Provimet.objects.values_list('course', flat=True).filter(student=request.user, afati=afati))

            courses = Course.objects.filter(program=program, year=year, semester=semester).exclude(pk__in=provimetList).annotate(hera=Count('pk'))

    return render (
        request, 'paraqit_provimet.html', {'program': program, 'courses': courses, 'provimet': provimet, 'afatet': afatet, 'afatetAll': afatetAll}, 
    )


def provimet_paraqitura(request):
    afatetAll = afatet_provimeve.objects.all()
    program = request.user.student.program
    provimet = None;

    if request.method == 'GET':
        if request.GET.get('filterProvimet'):
            if int(request.GET.get('afati')) >= 0:
                provimet = Provimet.objects.filter(student=request.user, afati=int(request.GET.get('afati')))

    # for p in Provimet.objects.raw('select "sems_provimet"."id", "sems_provimet"."course_id", count("sems_provimet"."course_id") as hera from "sems_provimet" group by "sems_provimet"."course_id"'):
    #     print(Course.objects.get(pk=p.course_id), p.hera)

    return render (
        request, 'provimet_paraqitura.html', {'program': program, 'provimet': provimet, 'afatetAll': afatetAll}, 
    )


def paraqit_provimin(request, c_pk, a_pk):
    course = Course.objects.get(pk=c_pk)
    provimet = Provimet()
    provimet.course = course
    provimet.student = request.user
    provimet.afati = afatet_provimeve.objects.get(pk=a_pk)
    provimet.time = datetime.now()
    provimet.refuzuar = False
    provimet.save()

    return redirect('provimet')
'''