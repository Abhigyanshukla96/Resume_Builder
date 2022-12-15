import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserDetails
from django.contrib.auth.models import User

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def get_user_details(user):
    return UserDetails.objects.filter(user=user).values()[0]

def create_resume(request):
    if request.method == 'GET':
        user = User.objects.get(username=request.user.username)
        if UserDetails.objects.filter(user=user).exists():
            data = get_user_details(request.user)
            return render(request, 'create_resume.html', context=data)
        return render(request, 'create_resume.html')
    
    if request.method=="POST":
        print("Submitting post request")
        user = User.objects.get(username=request.user.username)
        
        full_name=request.POST.get("name")
        address=request.POST.get("address")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        about_you=request.POST.get("about")
        education=request.POST.get("education")
        career=request.POST.get("career")
        job1_start= request.POST.get("job-1__start")
        job1_end= request.POST.get("job-1__end")
        job1_details= request.POST.get("job-1__details")
        job2_start=  request.POST.get("job-2__start")
        job2_end= request.POST.get("job-2__end")
        job2_details=request.POST.get("job-2__details")
        job3_start= request.POST.get("job-3__start")
        job3_end= request.POST.get("job-3__end")
        job3_details=request.POST.get("job-3__details")
        references=request.POST.get("references")
        
        data = {
                "user": user,
                "full_name": full_name,
                "address": address,
                "phone": phone,
                "email":email,
                "about_you":about_you,
                "education":education,
                "career":career,
                "job1_start":job1_start,
                "job1_end":job1_end,
                "job1_details":job1_details,
                "job2_start":job2_start,
                "job2_end":job2_end,
                "job2_details":job2_details,
                "job3_start":job3_start,
                "job3_end":job3_end,
                "job3_details":job3_details,
                }
        
        print("\n** Fetched Data: ", data)
        if UserDetails.objects.filter(user=user).exists():
            user_details_obj = UserDetails.objects.filter(user=user)
            user_details_obj.update(**data)
            messages.add_message(request, messages.INFO, 'Resume Info Edited Successfully. Download Resume Now')
            return redirect("create-resume")
        else:
            print("Saving data")
            user_details_obj = UserDetails(**data)
            user_details_obj.save()
            print("\nData Saved\n")
            messages.add_message(request, messages.INFO, 'Resume Info Saved Successfully. Download Resume Now')
            return redirect("resume")
        
        
def resume(request):
    try:
        resume_info = UserDetails.objects.filter(user__username=request.user.username).values()[0]
        context={"resume_info":resume_info}
        return render(request,"resume.html",context)
    except:
        return render(request,"resume.html")