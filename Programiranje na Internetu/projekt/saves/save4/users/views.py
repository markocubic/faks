from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, TemplateView
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


class MentorStudentiView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'users/profile/mentor_studenti.html'
    context_object_name = 'users'


class MentorStudentiRedovniView(ListView):
    model = CustomUser
    template_name = 'users/profile/mentor_studenti_redovni.html'
    context_object_name = 'users'


class MentorStudentiIzvanredniView(ListView):
    model = CustomUser
    template_name = 'users/profile/mentor_studenti_izvanredni.html'
    context_object_name = 'users'


@login_required #u ListView Klasu kasnije
def mentor_predmeti_view(request):
    return render(request, 'users/profile/mentor_predmeti.html')


@login_required
def student_view_pk(request, pk):
    context = {}
    user = CustomUser.objects.get(pk=pk)
    upisi = Upisi.objects.all()
    predmeti = Predmeti.objects.all()
    upisi_filtered = set()
    predmeti_filtered = set()

    if request.user.role == "student" and request.user.id != user.id:
        return redirect('/')

    flag=True
    for predmet in predmeti:
        for upis in upisi:
            if predmet.id == upis.predmet_id and user.id == upis.student_id:
                upisi_filtered.add(predmet)
                flag=False
        if flag:
            predmeti_filtered.add(predmet)
        flag=True
    
    if request.POST:
        for predmet in predmeti_filtered:
            if request.POST.get(str(predmet)):
                new = Upisi(student = user, predmet = predmet, status = "nepolozen")
                new.save()
                messages.success(request, "Dodano: " + predmet.ime)
        for upis_f in upisi_filtered:
            if request.POST.get(str(upis_f)):
                for upis in upisi:
                    if upis_f.id == upis.predmet_id and user.id == upis.student_id:
                        upis.delete()
                        messages.success(request, "Ispisano: " + upis_f.ime)
        return HttpResponseRedirect('/student/'+ str(pk) +'/')

    upisi_html = ""
    br_sem = 0  

    if user.status == "redovni":
        br_sem = 6
    elif user.status == "izvanredni":
        br_sem = 8

    for i in range(br_sem):
        upisi_html += "<p>Semestar " + str(i+1) + "</p>"
        upisi_html += "<table>"
        for upis in upisi_filtered:
            if user.status == "redovni":
                if upis.sem_redovni == i+1:
                    upisi_html += "<tr><td class='add-btn'><input type='submit' name='"+ str(upis) +"' value='U'></td>"
                    upisi_html += "<td class='add-btn'><input type='submit' name='"+ str(upis) +"' value='X'></td>"
                    upisi_html += "<td>" + upis.ime + "</td></tr>"
            if user.status == "izvanredni":
                if upis.sem_izvanredni == i+1:
                    upisi_html += "<tr><td class='add-btn'><input type='submit' name='"+ str(upis) +"' value='X'></td>"
                    upisi_html += "<td>" + upis.ime + "</td></tr>"
        upisi_html += "</table>"

    context = {
        'user' : user,
        'predmeti' : predmeti_filtered,
        'upisi' : upisi_html,
    }
    return render(request, 'users/profile/student.html', context)