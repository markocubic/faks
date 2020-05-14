from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import CustomUser, Predmeti, Upisi
from .forms import UserRegisterForm, UserAuthenticationForm

def registration_view(request):
    context = {}
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data['password1']
            account = authenticate(email=email, password=raw_password)
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('/login')
        else:
            context['registration_form'] = form
    else:
        form = UserRegisterForm()
        context['registration_form'] = form

    return render(request, 'users/register.html', context)


def login_view(request):
    context = {}
    user = request.user
    
    if user.is_authenticated:
        return redirect('/')

    if request.POST:
        form = UserAuthenticationForm(request.POST)

        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('/')
    else:
        form = UserAuthenticationForm()
    
    context['login_form'] = form
    return render(request, 'users/login.html', context)


def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')


@login_required
def mentor_view(request):
    return render(request, 'users/profile/mentor.html')

@login_required
def mentor_studenti_view(request):
    context={}
    users = CustomUser.objects.all()
    context['users'] = users
    return render(request, 'users/profile/mentor_studenti.html', context)

@login_required
def mentor_studenti_redovni_view(request):
    context={}
    users = CustomUser.objects.all()
    context['users'] = users
    return render(request, 'users/profile/mentor_studenti_redovni.html', context)

@login_required
def mentor_studenti_izvanredni_view(request):
    context={}
    users = CustomUser.objects.all()
    context['users'] = users
    return render(request, 'users/profile/mentor_studenti_izvanredni.html', context)

@login_required
def mentor_predmeti_view(request):
    return render(request, 'users/profile/mentor_predmeti.html')


@login_required
def student_view(request):
    context = {}
    upisi = Upisi.objects.all()
    predmeti = Predmeti.objects.all()
    upisi_filtered = set()
    predmeti_filtered = set()

    flag=True
    for predmet in predmeti:
        for upis in upisi:
            if predmet.id == upis.predmet_id and request.user.id == upis.student_id:
                upisi_filtered.add(predmet)
                flag=False
        if flag:
            predmeti_filtered.add(predmet)
        flag=True
    
    upisi = ""
    br_sem = 0

    if request.user.status == "redovni":
        br_sem = 6
    elif request.user.status == "izvanredni":
        br_sem = 8

    for i in range(br_sem):
        upisi += "<p>Semestar " + str(i+1) + "</p>"
        upisi += "<table>"
        for upis in upisi_filtered:
            if request.user.status == "redovni":
                if upis.sem_redovni == i+1:
                    upisi += "<tr><td>" + upis.ime + "</td></tr>"
            if request.user.status == "izvanredni":
                if upis.sem_izvanredni == i+1:
                    upisi += "<tr><td>" + upis.ime + "</td></tr>"
        upisi += "</table>"

    context = {
        'predmeti' : predmeti_filtered,
        'upisi' : upisi,
    }
    return render(request, 'users/profile/student.html', context)


