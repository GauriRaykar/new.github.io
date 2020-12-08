from django.shortcuts import render
from accounts import views
from .models import Submission
from .forms import SubmissionForm
from django.http import HttpResponse

from django.shortcuts import get_object_or_404
# Create your views here.

def next(request):
    return render(request,'next.html')

def Submission(request):
    question = request.POST.get("question")

    obj = Submission(question=question)
    obj.save();

    return render(request,'new.html',{"message":"Successfully Done!"})