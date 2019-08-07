from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import slugify
from django_fields import DefaultStaticImageField

class User(AbstractUser):
    is_student = models.BooleanField(default = False)
    is_assessor = models.BooleanField(default = False)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    SID = models.CharField(max_length=128, unique=True)
    stu_name = models.CharField(max_length=128, blank=True, default='')
    major = models.CharField(max_length=128)
    enroll_year = models.IntegerField
    graduate_year = models.IntegerField
    #assignment = models.ManyToManyField(Assignment)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.SID)
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return self.SID

class Module(models.Model):
    module_ID = models.CharField(max_length=128, unique=True)
    mod_name = models.CharField(max_length=128)
    SID = models.ForeignKey(Student,on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.module_ID

class Assessor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    assessor_ID = models.CharField(max_length=128, unique=True)
    ass_name = models.CharField(max_length=128)
    module_ID = models.ForeignKey(Module,on_delete=models.CASCADE)
    user_group = models.CharField(max_length=128)
    # academic or mentor
    institution = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Assessor, self).save(*args, **kwargs)

    def __str__(self):
        return self.assessor_ID

class Assignment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignments')
    assignment_ID = models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=1280)
    text = models.CharField(max_length=2560)
    SID = models.ForeignKey(Student,on_delete=models.CASCADE)
    module_ID = models.ForeignKey(Module,on_delete=models.CASCADE)
    assessor_ID = models.ForeignKey(Assessor,on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    student_slug = models.SlugField()
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.assignment_ID)
        self.student_slug = slugify(self.SID)
        super(Assignment, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Feedback(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    feedback_ID = models.CharField(max_length=128, unique=True)
    assignment_ID = models.ForeignKey(Assignment,on_delete=models.CASCADE)
    assessor_ID = models.ForeignKey(Assessor,on_delete=models.CASCADE)
    module_ID = models.ForeignKey(Module,on_delete=models.CASCADE)
    review_text = models.CharField(max_length=1280)
    #rating = models.ForeignKey(Rating)
    slug = models.SlugField(unique=True)
    assessor_slug = models.SlugField()
    assignment_slug = models.SlugField()
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.feedback_ID


class Competency(models.Model):
    com_name = models.CharField(max_length=128)
    group_ID = models.CharField(max_length=128)
    group_name = models.CharField(max_length=128)
    dimension_ID = models.CharField(max_length=128)
    dimension_name = models.CharField(max_length=128)
    competency_ID = models.CharField(max_length=128, unique=True)
    SID = models.ForeignKey(Student,on_delete=models.CASCADE)
    description = models.CharField(max_length=1280)
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name_plural = 'Competencies'

    def __str__(self):
        return self.com_name

class Student_comp(models.Model):
   # competency_ID = models.ForeignKey(Competency, unique=True)
    name = models.CharField(max_length=128)
    SID = models.ForeignKey(Student,on_delete=models.CASCADE, related_name='student_competency')
    semester = models.IntegerField(default=0)
    assignment_ID = models.ForeignKey(Assignment,on_delete=models.CASCADE)
    feedback_ID = models.ForeignKey(Feedback,on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    Module_ID = models.ForeignKey(Module,on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    student_slug = models.SlugField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    picture =DefaultStaticImageField(blank=True, default_image_path='default.png')
    
    def __str__(self):
        return self.user
