from django.urls import path
from . import views
from .views import error_department_access

urlpatterns = [
    path('university/<int:university_id>/', views.university_detail, name='university_detail'),
    
    # path('my_department/<int:university_id>/<int:department_id>/<int:course_id>/', views.my_department, name='my_department'),
    
    path('my_department/<int:university_id>/<int:department_id>/', views.my_department, name='my_department'),
    
    path('view_course/<int:course_id>/', views.view_course, name='view_course'),
    
    path('my_resources/<int:department_id>/<int:year>/<int:semester>/', views.my_resources, name='my_resources'),
    
    path('my_resources_selection/', views.my_resources_selection, name='my_resources_selection'),
    
    path('add_question/', views.add_question, name='add_question'),
    
    path('view_questions/<int:course_id>/', views.view_questions, name='view_questions'),
    
    path('view_questions/<int:question_id>/delete/', views.delete_question, name='delete_question'),
    
    path('submit-feedback/<int:question_id>/', views.submit_feedback, name='submit_feedback'),
   
    path('success-feedback/', views.success_feedback, name='success_feedback'),
    
    path('view_feedback/', views.view_feedback, name='view_feedback'),
    
    # path('resources/<int:question_id>/', views.view_resources, name='view_resources'),
    
    # path('get_departments/', views.get_departments, name='get_departments'),
    
    # path('select_department/', views.select_department, name='select_department'),
    
    # path('my_form/', views.my_form_view, name='my_form'),
    
    path('handle_love_click/<int:question_id>/', views.handle_love_click, name='handle_love_click'),
    
    path('share/<int:question_id>/', views.share_question, name='share_question'),

    path('ajax/load-departments/', views.load_departments, name='ajax_load_departments'), # AJAX
    
    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'), # AJAX
    
    # path('department_list/', views.nothing, name='nothing'),
    
    path('error/department/access-denied/', error_department_access, name='department_access_denied'),
    
    path('nothing/', views.nothing, name='nothing'),
]
