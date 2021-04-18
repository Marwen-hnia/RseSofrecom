from django.shortcuts import render

# Create your views here.
def AccueilView(request):
    return render(request,"index.html")