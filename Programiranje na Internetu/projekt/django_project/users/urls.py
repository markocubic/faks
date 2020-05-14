from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.registration_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('mentor/', views.mentor_view, name='mentor'),
    path('mentor_studenti/', views.mentor_studenti_view, name='mentor_studenti'),
    path('mentor_studenti_redovni/', views.mentor_studenti_redovni_view, name='mentor_studenti_redovni'),
    path('mentor_studenti_izvanredni/', views.mentor_studenti_izvanredni_view, name='mentor_studenti_izvanredni'),
    path('mentor_predmeti/', views.mentor_predmeti_view, name='mentor_predmeti'),
    path('mentor_predmeti_add/', views.mentor_predmeti_add_view, name='mentor_predmeti_add'),
    path('mentor_predmeti_edit/<int:pk>/', views.mentor_predmeti_edit_view, name='mentor_predmeti_edit'),
    path('student/<int:pk>/', views.student_view_pk, name='student'),

    
    #password reset urls
    path('password-reset/', 
        auth_views.PasswordResetView.as_view(template_name='users/password_reset/password_reset.html'), 
        name='password_reset'),

    path('password-reset/done/', 
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset/password_reset_done.html'), 
        name='password_reset_done'),
    
    path('password-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset/password_reset_confirm.html'), 
        name='password_reset_confirm'),
    
    path('password-reset-complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset/password_reset_complete.html'), 
        name='password_reset_complete'),
]
