from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from ESE.models import Subject, Student, Assessor, Assignment, Feedback, Competency, Module, Student_comp, User, Profile


class AssessorSignUpForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = User

	def save(self, commit=True):
		user = super().save(commit=False)
		user.is_assessor = True
		if commit:
			user.save()
		return user


class StudentSignUpForm(UserCreationForm):

	class Meta(UserCreationForm.Meta):
		model = User

	#@transaction.atomic
	def save(self, commit=True):
		user = super().save(commit=False)
		user.is_student = True
		if commit:
			user.save()
		return user

class StudentForm(forms.ModelForm):
	SID = forms.CharField(max_length=128, help_text="Please enter the student ID.")
	first_name = forms.CharField(max_length=128, help_text="Please enter the student's first name'.")
	surname = forms.CharField(max_length=128, help_text="Please enter the student's surname.")
	major = forms.CharField(max_length=128, help_text="Please enter the student's major.")
	enroll_year = forms.CharField(max_length=128, help_text="Please enter the student's year of enrollment.")
	graduate_year = forms.CharField(max_length=128, help_text="Please enter the student's year of graduation.")
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = Student
		fields = ('SID','first_name','surname','major','enroll_year','graduate_year',)

class ModuleForm(forms.ModelForm):
	module_ID = forms.CharField(max_length=128, help_text="Please enter the module ID.")
	name = forms.CharField(max_length=128, help_text="Please enter the module's name'.")
	#SID = forms.ModelChoiceField(queryset=Student.objects.all(), empty_label="Student ID")
	SID = forms.CharField(max_length=128,help_text="Please enter the student ID.")
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = Student
		exclude = ('slug',)

class AssessorForm(forms.ModelForm):
	assessor_ID = forms.CharField(max_length=128, help_text="Please enter the assessor ID.")
	first_name = forms.CharField(max_length=128, help_text="Please enter the assessor's first name'.")
	surname = forms.CharField(max_length=128, help_text="Please enter the assessor's surname.")
	module_ID = forms.CharField(max_length=128, help_text="Please enter the module ID.")
	user_group = forms.CharField(max_length=128, help_text="Please enter the user group of assessor.")
	institution = forms.CharField(max_length=128, help_text="Please enter the assessor's institution.")
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = Student
		exclude = ('slug',)


class AssignmentForm(forms.ModelForm):
	assignment_ID = forms.CharField(max_length=128, help_text="Please enter the assignment ID.")
	#SID = forms.ModelChoiceField(queryset=Student.objects.all(), empty_label="Student ID")
	title = forms.CharField(max_length=1280, help_text="Please enter the title of the assignment.")
	description = forms.CharField(max_length=1280, help_text="Please enter the description of the assignment.")
	text = forms.CharField(max_length=1280, help_text="Please enter the content of the assignment.")
	create_time = forms.DateTimeField()
	modify_time = forms.DateTimeField()
	SID = forms.CharField(max_length=128,help_text="Please enter the module ID.")
	module_ID = forms.CharField(max_length=128,help_text="Please enter the module ID.")
	assessor_ID = forms.CharField(max_length=128,help_text="Please enter the assessor ID.")
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	student_slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	#image = forms.ImageField(required=False, help_text="Please upload the picture of the recipe." )

	class Meta:
		model = Assignment
		exclude = ('assessor_ID','student_slug', 'slug',)


class FeedbackForm(forms.ModelForm):
	assignment_ID = forms.CharField(max_length=128, help_text="Please enter the assignment ID.")
	#SID = forms.ModelChoiceField(queryset=Student.objects.all(), empty_label="Student ID")
	feedback_ID = forms.CharField(max_length=128)
	SID = forms.CharField(max_length=128,help_text="Please enter the student ID.")
	module_ID = forms.CharField(max_length=128,help_text="Please enter the module ID.")
	review_text = forms.CharField(max_length=1280, help_text="Please enter the content of the feedback.")
	create_time = forms.DateTimeField()
	modify_time = forms.DateTimeField()
	assessor_ID = forms.CharField(max_length=128,help_text="Please enter the assessor ID.")
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	assignment_slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	assessor_slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	#image = forms.ImageField(required=False, help_text="Please upload the picture of the recipe." )

	class Meta:
		model = Assignment
		exclude = ('assignment_slug','assessor_slug', 'slug',)

class CompetencyForm(forms.ModelForm):
	competency_ID = forms.CharField(max_length=128, help_text="Please enter the competency ID.")
	name = forms.CharField(max_length=128, help_text="Please enter the name of the competency.")
	group_ID = forms.CharField(max_length=128, help_text="Please enter the group ID of the competency.")
	group_name = forms.CharField(max_length=128, help_text="Please enter the group name of the competency.")
	dimension_ID = forms.CharField(max_length=128, help_text="Please enter the dimension ID of the competency.")
	dimension_name = forms.CharField(max_length=128, help_text="Please enter the dimension name of the competency.")
	description = forms.CharField(max_length=1280, help_text="Please enter the description of the competency.")
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = Student
		exclude = ('slug',)

class Student_compForm(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text="Please enter the name of the competency.")
	SID = forms.ModelChoiceField(queryset=Student.objects.all(), empty_label="Student ID")
	module_ID = forms.CharField(max_length=128, help_text="Please enter the module ID.")
	semester = forms.CharField(max_length=1280, help_text="Please enter the semester.")
	assignment_ID = forms.CharField(max_length=128, help_text="Please enter the assignment ID.")
	feedback_ID = forms.CharField(max_length=128)
	semester = forms.CharField(max_length=1280, help_text="Please enter the rating of the competency.")
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	student_slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = Student
		exclude = ('slug', 'student_slug',)

class ContactForm(forms.Form):
	name = forms.CharField(max_length=100)
	email = forms.EmailField()
	message = forms.CharField(widget=forms.Textarea)

'''
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password',)
'''
class ProfileForm(forms.ModelForm):
	picture = forms.ImageField(required=False)

	class Meta:
		model = Profile
		exclude = ('user',)
