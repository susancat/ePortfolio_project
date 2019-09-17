from django.urls import reverse, resolve
from django.test import TestCase
from .views import home_view, modules_view, module_add, module_detail, students_view, student_detail, competency_detail, update_assessor, competency_edit, competency_delete, user_edit, select_assessor, rating_students
from .models import Module, Competency, User, Upload, Student, Rating

class HomePageTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

class ModulesTests(TestCase):
    def setUp(self):
        Module.objects.create(name='Algorithm',summary='for year-3 students',year='3',semester='6',level='Bachelor')

    def test_module_view_success_status_code(self):
        url = reverse('modules')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

class StudentsTests(TestCase):
    def setUp(self):
        Student.objects.create(first_name='Arya',last_name='Stark',email='AryaS@gmail.com',major='Software Engineering')

    def test_student_view_success_status_code(self):
        url = reverse('students')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

class CompetenciesTests(TestCase):
    def setUp(self):
        Competency.objects.create(name='High auto_esteem',description='has high dignity to push he/she achieve accomplishment',group_name='Personals',dimension_name='Personal development')

    def test_competency_view_success_status_code(self):
        url = reverse('filter_views')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


class ViewTests(TestCase):

    def setUp(self):
        try:
            from forms import ModuleForm
            from forms import CompetencyAddForm
            from forms import RatingStudentsForm
            from forms import SelectAssessorsForm

        except ImportError:
            print('The module forms does not exist')
        except NameError:
            print('The form does not exist or is not correct')
        except:
            print('Something else went wrong :-(')

    pass