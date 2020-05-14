from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, TemplateView, UpdateView
from .models import CustomUser, Predmeti, Upisi
from .forms import UserRegisterForm, UserAuthenticationForm, PredmetForm, PredmetForm

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
            return HttpResponseRedirect(reverse('login'))
        else:
            context['registration_form'] = form
    else:
        form = UserRegisterForm()
        context['registration_form'] = form
    context['title'] = 'Register'

    return render(request, 'users/register.html', context)


def login_view(request):
    context = {}
    user = request.user
    
    if user.is_authenticated:
        return HttpResponseRedirect(reverse('sveuciliste-home'))

    if request.POST:
        form = UserAuthenticationForm(request.POST)

        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('sveuciliste-home'))
    else:
        form = UserAuthenticationForm()
    
    context['login_form'] = form
    context['title'] = 'Login'
    return render(request, 'users/login.html', context)


def logout_view(request):
    logout(request)

    context = {}
    context['title'] = 'Logout'
    return render(request, 'users/logout.html', context)


@login_required
def mentor_view(request):
    if request.user.role != "mentor":
        return HttpResponseRedirect(reverse('sveuciliste-home'))
    context = {}
    context['title'] = str(request.user.email)
    return render(request, 'users/profile/mentor.html', context)

@login_required
def mentor_studenti_view(request):
    context = {}
    users = CustomUser.objects.all()
    if request.user.role != "mentor":
        return HttpResponseRedirect(reverse('sveuciliste-home'))
    context = {
        'users' : users,
        'title' : str(request.user.email),
    }
    return render(request, 'users/profile/mentor_studenti.html', context)

@login_required
def mentor_studenti_redovni_view(request):
    context = {}
    users = CustomUser.objects.all()
    if request.user.role != "mentor":
        return HttpResponseRedirect(reverse('sveuciliste-home'))
    context = {
        'users' : users,
        'title' : str(request.user.email),
    }
    return render(request, 'users/profile/mentor_studenti_redovni.html', context)

@login_required
def mentor_studenti_izvanredni_view(request):
    context = {}
    users = CustomUser.objects.all()
    if request.user.role != "mentor":
        return HttpResponseRedirect(reverse('sveuciliste-home'))
    context = {
        'users' : users,
        'title' : str(request.user.email),
    }
    return render(request, 'users/profile/mentor_studenti_izvanredni.html', context)

@login_required
def mentor_predmeti_view(request):
    if request.user.role != "mentor":
        return HttpResponseRedirect(reverse('sveuciliste-home'))
    context = {}
    predmeti = Predmeti.objects.all()

    if request.POST:
        for predmet in predmeti:
            if request.POST.get(str(predmet)) == 'delete':
                messages.success(request, "Izbrisano: " + str(predmet.ime))
                predmet.delete()
                return HttpResponseRedirect(reverse('mentor_predmeti'))
            elif request.POST.get(str(predmet)) == 'edit':
                return HttpResponseRedirect(reverse('mentor_predmeti_edit', args=(predmet.id,)))
    context = {
        'predmeti' : predmeti,
        'title' : str(request.user.email),
    }
    return render(request, 'users/profile/mentor_predmeti.html', context)


@login_required
def student_view_pk(request, pk):
    context = {}
    user = CustomUser.objects.get(pk=pk)
    upisi = Upisi.objects.all()
    predmeti = Predmeti.objects.all()
    upisi_filtered = set()
    predmeti_filtered = set()

    if request.user.role == "student" and request.user.id != user.id:
        return HttpResponseRedirect(reverse('sveuciliste-home'))

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
                messages.success(request, "Upisano: " + predmet.ime)
        for upis_f in upisi_filtered:
            if request.POST.get(str(upis_f)):
                for upis in upisi:
                    if upis_f.id == upis.predmet_id and user.id == upis.student_id:
                        if request.POST.get(str(upis_f)) == "not_passed":
                            upisi.filter(pk=str(upis.id)).update(status="nepolozen")
                            messages.success(request, "Nije položeno: " + upis_f.ime)
                        elif request.POST.get(str(upis_f)) == "passed":
                            upisi.filter(pk=str(upis.id)).update(status="polozen")
                            messages.success(request, "Položeno: " + upis_f.ime)
                        elif request.POST.get(str(upis_f)) == "remove":
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
        upisi_html += "<div class='semestar'>"
        upisi_html += "<p>Semestar " + str(i+1) + ":</p>"
        upisi_html += "<table>"
        for upis in upisi:
            predmet = predmeti.get(pk = str(upis.predmet_id))
            if user.id == upis.student_id:
                if user.status == "redovni" and predmet.sem_redovni == i+1:
                        if upis.status == "polozen":
                            upisi_html += "<tr><td></td><td><button type='submit' class='add-btn' name='"+ str(predmet) +"' value='not_passed'>&#10004;</button></td>"
                        elif upis.status == "nepolozen":
                            upisi_html += "<tr><td><button type='submit' class='add-btn' name='"+ str(predmet) +"' value='passed'>&#10004;</button></td>"
                            upisi_html += "<td><button type='submit' class='add-btn' name='"+ str(predmet) +"' value='remove'>&#10006;</button></td>"
                        upisi_html += "<td>" + predmet.ime + "</td></tr>"
                elif user.status == "izvanredni" and predmet.sem_izvanredni == i+1:
                        if upis.status == "polozen":
                            upisi_html += "<tr><td></td><td><button class='add-btn' type='submit' name='"+ str(predmet) +"' value='not_passed'>&#10004;</button></td>"
                        elif upis.status == "nepolozen":
                            upisi_html += "<tr><td><button type='submit' class='add-btn' name='"+ str(predmet) +"' value='passed'>&#10004;</button></td>"
                            upisi_html += "<td><button type='submit' class='add-btn' name='"+ str(predmet) +"' value='remove'>&#10006;</button></td>"
                        upisi_html += "<td>" + predmet.ime + "</td></tr>"
        upisi_html += "</table>"
        upisi_html += "</div>"

    context = {
        'user' : user,
        'predmeti' : predmeti_filtered,
        'upisi' : upisi_html,
        'title' : user.email,
    }
    return render(request, 'users/profile/student.html', context)


@login_required
def mentor_predmeti_add_view(request):
    if request.user.role != "mentor":
        return HttpResponseRedirect(reverse('sveuciliste-home'))
    context = {}
    if request.method == 'POST':
        form = PredmetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Predmet has been created!')
            return HttpResponseRedirect(reverse('mentor_predmeti'))
        else:
            context['predmet_add_form'] = form
    else:
        form = PredmetForm()
        context['predmet_add_form'] = form
    context['title'] = str(request.user.email)

    return render(request, 'users/profile/mentor_predmeti_add.html', context)

@login_required
def mentor_predmeti_edit_view(request, pk):
    if request.user.role != "mentor":
        return HttpResponseRedirect(reverse('sveuciliste-home'))
    predmet = Predmeti.objects.get(pk=pk)
    context = {}
    if request.method == 'POST':
        form = PredmetForm(request.POST, instance=predmet)
        if form.is_valid():
            form.save()
            messages.success(request, f'Predmet has been edited!')
            return HttpResponseRedirect(reverse('mentor_predmeti'))
        else:
            context['predmet_edit_form'] = form
    else:
        form = PredmetForm(instance=predmet)
        context['predmet_edit_form'] = form
    context['predmet'] = predmet
    context['title'] = str(request.user.email)
    
    return render(request, 'users/profile/mentor_predmeti_edit.html', context)

