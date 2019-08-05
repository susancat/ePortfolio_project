from django.urls import include, path
from django.conf.urls import url
from ESE.views import ESE, students, assessors

urlpatterns = [
    path('', ESE.home, name='home'),
    path('about', ESE.about, name='about'),
    path('contact_us', ESE.contact_us, name='contact_us'),
    
    #url(r'^register_profile/$', ESE.register_profile, name='register_profile'),
    path('show_assessor', ESE.show_assessor, name='show_assessor'),
    path('show_student', ESE.show_student, name='show_student'),
    path('show_assignment', ESE.show_assignment, name='show_assignment'),
    path('show_feedback', ESE.show_feedback, name='show_feedback'),
    path('show_competency', ESE.show_competency, name='show_competency'),
    path('show_studentcomp', ESE.show_studentcomp, name='show_studentcomp'),

    path('students/', include(([
        path('add_assignment', students.add_assignment, name='add_assignment'),
        path('student_dashboard',students.student_dashboard, name='student_dashboard'),
    ], 'ESE'), namespace='students')),

    path('assessors/', include(([
        path('add_competency', assessors.add_competency, name='add_competency'),
        path('add_feedback', assessors.add_feedback, name='add_feedback'),
        path('assessor_dashboard',assessors.assessor_dashboard, name='assessor_dashboard'),
    ], 'ESE'), namespace='assessors')),
]
