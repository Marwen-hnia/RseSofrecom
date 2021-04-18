from django.shortcuts import render


# Create your views here.
from authentication.models import User


def AmisView(request):
    user=[]
    print("Search User")
    if 'recherche' in request.GET:
        recherche=request.GET['recherche']
        user=User.objects.all().filter(nom_dept__icontains=recherche)
        print(user)
    if request.method=='POST':
        print("View Profile")
    context={
    'user':user,
    }
    return render(request, "examples-contacts.html",context)
