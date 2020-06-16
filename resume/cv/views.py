from django.shortcuts import render
from.models import About,Experience,Education,Skill,Interest,Award

def index(request):
    about=About.objects.all()
    experience=Experience.objects.all()
    education=Education.objects.all()
    skil = Skill.objects.all()
    interest = Interest.objects.all()
    awrd = Award.objects.all()
    context={
        'about':about,
        'experience':experience,
        'education':education,
        'skil':skil,
        'interest':interest,
        'awrd':awrd

    }

    return render(request,'index.html',context)
