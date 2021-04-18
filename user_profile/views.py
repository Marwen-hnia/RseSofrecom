from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from authentication.models import User, CompetenceModel, FormationModel

import json


def getprofileData(request):
        comt = []
        formation = []
        poste=[]

        cmptNoteArr=[]

        expDt={}
        comptenc = list(CompetenceModel.objects.all().values('competences'))
        ecole = list(FormationModel.objects.all().values('name'))
        for c in comptenc:
            comt.append(c.get("competences"))

        for f in ecole:
            formation.append(f.get("name"))
        user = User.objects.filter(mail__icontains=request.user.email)[0]

        mat_emp = user.mat_emp
        mat = mat_emp.lstrip("0")
        for i in range(len(user.post)):
            expDt = {
                "exp": user.post[i],
                "date": user.datede[i],
                'fin': user.adate[i]
            }

        poste.append(expDt)


        for i in range(len(user.comeptence)):
            cmptNote= {
                "cmpt":user.comeptence[i],
                "note":int(user.note[i].strip('/5'))
            }
        cmptNoteJson = json.dumps(cmptNote)
        print(cmptNoteJson)


        if user.resp_bu == "NULL" and user.name_bu == "NULL":
            user.resp_bu = user.nom_resp
            user.name_bu = user.nom_dept
        if request.method=='POST':
            Adresse_résidence = request.POST.get("Adresse_résidence")
            Adresse_domicile=request.POST.get("Adresse_domicile")
            Telephone_professionnel = request.POST.get("Telephone_professionnel")
            Téléphone_personnel = request.POST.get("Téléphone_personnel")
            Date_de_naissance=request.POST.get("Date_de_naissance")
            LinkedIn=request.POST.get("LinkedIn")
            poste=request.POST.getlist("poste[]")
            datede=request.POST.getlist("datede[]")
            adate = request.POST.getlist("adate[]")






            frmtion=request.POST.get("formation")
            vie_associative=request.POST.get("vie_associative")
            competence = request.POST.getlist("competences[]")
            note = request.POST.getlist("note[]")
            User.objects.filter(mail__icontains=request.user.email).update(adresse_residence=Adresse_résidence,
                             adresse_domicile=Adresse_domicile,Telephone_professionnel=Telephone_professionnel,
                             Telephone_personnel=Téléphone_personnel,linkedin=LinkedIn,post=poste,datede=datede,adate=adate,
                             formation=frmtion,vie_associative=vie_associative,date_de_naissance=Date_de_naissance,comeptence=competence,note=note)

        context = {
            'user': user,
            'mat': mat,
            'compt': comt,
            'formation': formation,
            'post':poste,
            'cmptNote':cmptNoteArr



        }

        return render(request, "examples-profile.html", context)
