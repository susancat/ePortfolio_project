from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from datetime import datetime
from django import forms
from django.db.models.signals import post_save


RATING = (
    (0, 'Not Demostrated'), 
    (1, 'Weak'),
    (2, 'Strong'),
)


DAYS = (
    [(i, i) for i in range(1, 31)]
)

MONTHS = (
    (1, 'Jan'),
    (2, 'Feb'),
    (3, 'Mar'),
    (4, 'Apr'),
    (5, 'May'),
    (6, 'June'),
    (7, 'Jul'),
    (8, 'Aug'),
    (9, 'Sep'),
    (10, 'Oct'),
    (11, 'Nov'),
    (12, 'Dec'),
)

YEARS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    )

SEMESTER = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
    )

LEVELS = (
    ('Bachelor', 'Bachelor'),
    ('Master', 'Master'),
)


class Module(models.Model):
    name = models.CharField(max_length=150)
    summary = models.TextField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    year = models.IntegerField(choices=YEARS, default=1)
    semester = models.IntegerField(choices=SEMESTER, default=1)
    level = models.CharField(max_length=100, choices=LEVELS, default='Bachelor')

    def __str__(self):
        return self.name


class Competency(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=600, null=True, blank=True)
    module = models.ManyToManyField(Module, related_name='competencies', blank=True)
    group_name = models.CharField(max_length=128)
    dimension_name = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'Competencies'

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    #SID = models.CharField(max_length=128, unique=True)
    picture = models.ImageField(null=True, blank=True, default='no-img.png')
    email = models.EmailField(max_length=100, null=True)
    major = models.CharField(max_length=100, null=True)
    country = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    city = models.CharField(max_length=100, null=True)
    module = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True)
    assessor = models.ManyToManyField(Competency, related_name='assessor', blank=True)
    year = models.IntegerField(choices=YEARS, default=1)
    competency = models.ManyToManyField(Competency, related_name='competency', blank=True)
    semester = models.IntegerField(choices=SEMESTER, default=1)
    level = models.CharField(max_length=100, choices=LEVELS, default=1)

    def __str__(self):
        if self.first_name and not self.last_name:
            return self.first_name
        elif self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        else:
            return 'Student'


def create_profile(sender, **kwargs):
    if kwargs['created']:
        student = Student.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)


class New(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    picture = models.ImageField(null=True, blank=True)
    create_date = models.DateTimeField(default=datetime.now)

    def get_content(self):
        return self.content[:150] + '...'

    def __str__(self):
        return self.title


class Rating(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    competency = models.ForeignKey(Competency, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING, default=0)

    def __str__(self):
        return self.student.student.first_name + ' ' + self.student.student.last_name


class Upload(models.Model):
    name = models.CharField(max_length=100)
    competency = models.ForeignKey(Competency, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/', validators=[FileExtensionValidator(['pdf', 'docx', 'doc', 'xls', 'xlsx', 'ppt', 'pptx', 'zip', 'rar', '7zip'])])
    upload_time = models.DateTimeField(default=datetime.now, null=True)

    def get_extension_short(self):
        ext = str(self.file).split(".")
        ext = ext[len(ext)-1]

        if ext == 'doc' or ext == 'docx':
            return 'word'
        elif ext == 'pdf':
            return 'pdf'
        elif ext == 'xls' or ext == 'xlsx':
            return 'excel'
        elif ext == 'ppt' or ext == 'pptx':
            return 'powerpoint'
        elif ext == 'zip' or ext == 'rar' or ext == '7zip':
            return 'archive'

    def __str__(self):
        return str(self.file)[6:]



def get_full_name(self):
    if self.student.first_name and self.student.last_name:
        return self.student.first_name + ' ' + self.student.last_name
    return self.username

User.add_to_class("__str__", get_full_name)