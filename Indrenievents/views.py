from django.shortcuts import render,redirect
from django.http import response
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, get_user_model
from .forms import RegistrationForm, AddeventForm
from .models import Student, Addnewevent

# Create your views here.
def testpage(request,*args,**kwargs):
    content={
    }
    return render(request,'base.html',content) 


def registrationpage(request,*args,**kwargs):
    my_form=RegistrationForm(request.GET)
    if request.method== "POST":
        my_form=RegistrationForm(request.POST)
        if my_form.is_valid():
            studentname=my_form.cleaned_data.get('Student_name')
            email=my_form.cleaned_data.get('Email')
            password=my_form.cleaned_data.get('Password')
            my_form.save()
            if User.objects.filter(email=email):
                messages.info(request,"Email Already taken")
                return redirect('register')
            else:
                user1=User.objects.create_user(username=studentname,email=email,password=password)
                user1.save()
                messages.success(request,f'Account created for {studentname}')
                return redirect('login')
    content={
        "form": my_form

    }
    return render(request,'registrationpage.html',content)


def loginpage(request,*args,**kwargs):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user= authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,f'Login successful')
            return redirect('home')
        else:
            messages.warning(request,'Login Failed. Please try again with correct email and password')
            return redirect('login')
    else:
        data={
        }
        return render(request,'studentlogin.html',data)

def homepage(request,*args,**kwargs):
    content={

    }
    return render(request,'homepage.html',content)



def addeventpage(request,*args,**kwargs):
    
    if request.method=="POST":
        mineform=AddeventForm(request.POST,request.FILES)
        if mineform.is_valid():
            eventname=mineform.cleaned_data.get('Eventname')
            mineform.save()
            messages.success(request,f'Event {eventname} is added successfully')
            mineform=AddeventForm(request.GET)
            return redirect('home')
        else:
            messages.warning(request,"form is not valid")
            return redirect('addevent')
    else:
        mineform=AddeventForm(request.GET)
    context={
        "form2":mineform
    }
    return render(request,'addevent.html',context)


def vieweventpage(request,*args,**kwargs):
    allevents=Addnewevent.objects.all()
    context={
        "showallevents":allevents,
        
    }
    return render(request,'viewevent.html',context)



def eventdetailspage(request,*args,**kwargs):
    allevent=Addnewevent.objects.all()
    context={
        "allevent":allevent
    }
    return render(request,'eventdetails.html',context)


        
    




# # message.debug
# # message.error
# # message.info
# # message.success
# # message.warning
# # if not user:
#             #     raise myform.error("This user doesnot exist")
#             # if not user.check_password(password):
#             #     raise myform.error("Incorrect Password")
#             # if not user.is_active:
#             #     raise myform.error("User is not active") 
#             # if not user.check_email(email):
#             #     raise myform.error("Incorrect email")