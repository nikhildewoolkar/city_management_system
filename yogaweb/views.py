from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.core.exceptions import ObjectDoesNotExist
import datetime
from datetime import datetime
import os
from django.conf import settings 
from django.core.mail import send_mail 
import numpy as np
from django.contrib import messages
from subprocess import check_output, CalledProcessError,STDOUT
from django.contrib.auth.models import User, auth
from django.http import HttpResponse, request
from .models import UserProfile,Newsletter,Contact,Issue
def home(request):
    return render(request,"home.html")

def contact(request):
    if request.method=='POST':
        g=0
        name=request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        message=request.POST.get("message")
        c=Contact(name=name,email=email,sub=subject,msg=message)
        c.save()
        try:
            subject = 'Query/Suggestion Received'  
            message = f'Hi{name}--{email},Your response is received by Yoga class app.We will reply as soon as possible.'
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = [email] 
            send_mail( subject, message, email_from, recipient_list ,fail_silently=False)
            messages.info(request,'Query/Feedback Submitted.we will reply you soon.')
        except:
            messages.info(request,'Query/Feedback Submitted.we will reply you soon.')
        return render(request,"contact.html",{"g":g}) 
    return render(request,"contact.html")
def signup(request):
    if request.method=='POST':
        first_name=request.POST.get("fname")
        last_name=request.POST.get("lname")
        email=request.POST.get("email")
        username=email
        mobno=request.POST.get("phoneno")
        ward=request.POST.get("ward")
        area=request.POST.get("area")
        city=request.POST.get("city")
        taluka=request.POST.get("taluka")
        district=request.POST.get("district")
        state=request.POST.get("state")
        pincode=request.POST.get("pincode")
        utype=request.POST.get("utype")
        password=request.POST.get("pass")
        password1=request.POST.get("pass1")
        def password_check(password):
            SpecialSym =['$', '@', '#', '%']
            val = True
            if len(password) < 8:
                print('length should be at least 6') 
                val = False
            if len(password) > 20: 
                print('length should be not be greater than 8') 
                val = False
            if not any(char.isdigit() for char in password): 
                print('Password should have at least one numeral') 
                val = False
            if not any(char.isupper() for char in password): 
                print('Password should have at least one uppercase letter') 
                val = False
            if not any(char.islower() for char in password): 
                print('Password should have at least one lowercase letter') 
                val = False
            if not any(char in SpecialSym for char in password): 
                print('Password should have at least one of the symbols $@#') 
                val = False
            if val == False: 
                val=True
                return val
        if (password_check(password)): 
            print("y")
        else: 
            print("x")                 
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('signup')
            elif (password_check(password)):
                messages.info(request,'password is not valid(must be combination of (A-Z,a-z,@,1-9))')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,"user created succesfully")
                user=auth.authenticate(username=username,password=password)
                if user is not None:
                   auth.login(request,user)
                u = User.objects.get(username=username)
                reg=UserProfile(user=u,utype=utype,usernames=username,phoneno=mobno,area=area,city=city,taluka=taluka,district=district,state=state,pincode=pincode,wardno=ward,password=password)
                reg.save()
                auth.logout(request)
        else:
            messages.info(request,"password not matching")
            return redirect('signup')
        return redirect('login')
    return render(request,"signup.html")
def login(request):
    if request.method=="POST":
        username=request.POST.get("email")
        password=request.POST.get("pwd")
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request,"Login successful")
            return render(request,"home.html")
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return render(request,"login.html")
def profile(request):
    if request.method=="POST":
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        username=request.POST.get("username")
        mobno=request.POST.get("phoneno")
        ward=request.POST.get("ward")
        area=request.POST.get("area")
        city=request.POST.get("city")
        taluka=request.POST.get("taluka")
        district=request.POST.get("district")
        state=request.POST.get("state")
        pincode=request.POST.get("pincode")
        utype=request.POST.get("utype")
        User.objects.filter(username=username).update(first_name=fname,last_name=lname)
        UserProfile.objects.filter(usernames=username).update(utype=utype,usernames=username,phoneno=mobno,area=area,city=city,taluka=taluka,district=district,state=state,pincode=pincode,wardno=ward)
        messages.info(request,"Profile Updated Properly")
        return render(request,"profile.html")    
    return render(request,"profile.html")
    
def newsletter(request):
    if request.method=="POST":
        g=1
        email=request.POST.get("email")
        d=Newsletter.objects.all()
        for d in d:
            if(email == d.email):
                messages.info(request,"Email already present in Newsletter database.")
                break
        else:
            wo=Newsletter(email=email)
            wo.save()
            try:
                subject = 'Newsletter Activated'   
                message = f'Hi {email},Newsletter Activated for your entered email address.Now you will get all the updates from yoga class app.'
                email_from = settings.EMAIL_HOST_USER 
                recipient_list = [email] 
                send_mail( subject, message, email_from, recipient_list ,fail_silently=False)
                messages.info(request,"Newsletter Activated.")
            except:
                messages.info(request,"Newsletter Activated.")
        return render(request,"contact.html",{"g":g})   
    return render(request,"contact.html")

def changepassword(request):
    if request.method == 'POST':
        old=request.POST.get("old")
        new1=request.POST.get("new1")
        new2=request.POST.get("new2")
        def passwordcheck(password):
            SpecialSym =['$', '@', '#', '%'] 
            val = True
            if len(password) < 8:
                print('length should be at least 8') 
                val = False
            if len(password) > 20: 
                print('length should be not be greater than 20') 
                val = False
            if not any(char.isdigit() for char in password): 
                print('Password should have at least one numeral') 
                val = False
            if not any(char.isupper() for char in password): 
                print('Password should have at least one uppercase letter') 
                val = False
            if not any(char.islower() for char in password): 
                print('Password should have at least one lowercase letter') 
                val = False
            if not any(char in SpecialSym for char in password): 
                print('Password should have at least one of the symbols $@#') 
                val = False
            return val
        p=request.user
        u1 = UserProfile.objects.get(usernames=p.username)
        if(u1.password==old):
            if(new1==new2):
                password=new1
                if(passwordcheck(password)==True):
                    u = User.objects.get(username=p.username)
                    u.set_password(new1)
                    u.save()
                    UserProfile.objects.filter(usernames=p.username).update(password=new1)
                    messages.info(request,"password Changed succesfully.Login using new Password.")
                    return redirect('logout')
                else:
                    messages.info(request,"Password should contain(0-9,a-z,A-Z,@)")
                    return render(request,"changepassword.html")    
            else:
                messages.info(request,"Password Don't Match")
                id=3
                return render(request,"changepassword.html",{"id":id})
        else:
            messages.info(request,"Old Password is not Correct or error occured.")
            id=3
            return render(request,"changepassword.html",{"id":id})
    id=3
    return render(request,"changepassword.html",{"id":id})

def viewissue(request):
    p1=request.user
    if(p1.userprofile.utype=="citizen"):
        n=Issue.objects.filter(auther=p1.username)
    if(p1.userprofile.utype=="wardadmin"):
        n=Issue.objects.filter(areaadmin=p1.username)
    return render(request,"viewissue.html",{'n':n})

def resendpass(request):
    if request.method == 'POST':
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        username=request.POST.get("email")
        phoneno=request.POST.get("phoneno")
        u=1
        try:
            p=User.objects.get(username=username)
            pa=UserProfile.objects.get(usernames=username)
        except:
            u=0
        if(u==1):
            password=pa.password
            if(fname == p.first_name and lname == p.last_name and phoneno ==pa.phoneno):
                print(0)
                try:
                    print(2)
                    subject = 'Forget Password(Resend)'   
                    message = f'Hi {p.username},your password for the Yoga Class app {password}. try logging in once again and change the password.'
                    email_from = settings.EMAIL_HOST_USER 
                    recipient_list = [p.email] 
                    send_mail( subject, message, email_from, recipient_list ,fail_silently=False)
                    messages.info(request,"password has been sent to your registered email address,kindly check.")
                except:
                    print(1)
                    messages.info(request,"sorry for inconvenience.email sending fail. kindly send query on conact page with proper subject and text.we will contact you soon..")
            else:
                messages.info(request,"Entered incorrect information.Try using correct credentials.")
            return render(request,"resendpass.html")
        else:
            messages.info(request,"User is not registered.kindly go to signup page and register.")
            return render(request,"login.html")
        return render(request,"login.html")
    return render(request,"resendpass.html")

def addissue(request):
    n=UserProfile.objects.filter(utype="wardadmin")
    p1=request.user
    if request.method=="POST":
        header=request.POST.get("header")
        text=request.POST.get("text")
        uid=request.POST.get("uid")
        j=UserProfile.objects.get(usernames=uid)
        area=j.area
        wardno=j.wardno
        city=j.city
        taluka=j.taluka
        district=j.district
        state=j.state
        pincode=j.pincode
        auther=p1.username
        phoneno=p1.userprofile.phoneno
        email=p1.email
        date=datetime.now()
        fo=Issue(auther=auther,phoneno=phoneno,email=email,header=header,text=text,date=date,areaadmin=uid,area=area,wardno=wardno,city=city,taluka=taluka,district=district,state=state,pincode=pincode,status="requested")
        fo.save()
        messages.info(request,"Issue has been uploaded successfully.Wait for admin response to proceed further.")
    return render(request,"addissue.html",{'n':n})
