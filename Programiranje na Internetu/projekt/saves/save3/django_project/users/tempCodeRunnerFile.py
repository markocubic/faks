def student_view(request):
    context = {}
    predmeti = Predmeti.objects.all()
    print(predmeti.id)
    upisi = Upisi.objects.all()
    context = {
        'predmeti' : predmeti,
        'upisi' : upisi,
    }
    return render(request, 'users/profile/student.html', context)