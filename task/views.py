from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# from .forms import submisssionForms
# from .models import submission

# Create your views here.
def home(request):
    return render(request,'index.html')


def profile(request):
    return render(request,'profile.html')

def pdf(request):
    return render(request,'pdf.html')

def new(request):
    return render(request,'new.html')

def video(request):
    return render(request,'video.html')

# def submission(request):
#     if request.method == "POST":
#         form = submisssionForms(request.POST)
#         if form.is_valid():

#             question=request.get["question",""]
#             obj = submission(question=question)
#             obj.save()

#             return HttpResponseRedirect(reverse("submission"))

#     else:
#         form = submissionForm()

#     return render(request,'index.html',{
#         'form': form,
#     })



    