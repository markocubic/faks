from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.registration_view, name='register'),
    path('logout/', user_views.logout_view, name='logout'),
    path('login/', user_views.login_view, name='login'),
    path('mentor/', user_views.mentor_view, name='mentor'),
    path('mentor_studenti/', user_views.mentor_studenti_view, name='mentor_studenti'),
    path('mentor_studenti_redovni/', user_views.mentor_studenti_redovni_view, name='mentor_studenti_redovni'),
    path('mentor_studenti_izvanredni/', user_views.mentor_studenti_izvanredni_view, name='mentor_studenti_izvanredni'),
    path('mentor_predmeti/', user_views.mentor_predmeti_view, name='mentor_predmeti'),
    path('student/', user_views.student_view, name='student'),
    path('', include('sveuciliste.urls')),

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