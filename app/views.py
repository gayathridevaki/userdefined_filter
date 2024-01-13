from django.shortcuts import render

# Create your views here.
def userfilter(request):
    d={'data':'Hi how ARE you'}
    return render(request,'userfilter.html',d)
