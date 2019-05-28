from django.shortcuts import render
from .models import Job

# Create your views here.
def home(request):
	jobs=Job.objects # this Job model is imported to use python objects
	return render(request,'jobs/home.html',{'jobs':jobs})