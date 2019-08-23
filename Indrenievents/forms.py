from django import forms
from .models import Student, Addnewevent
from django.contrib.auth.models import auth 
import datetime
# from django.contrib.auth import authenticate

class RegistrationForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput)
    class Meta:        
        model=Student
        fields=[
            'Student_name',
            'College_name',
            'Faculty',
            'Semester',
            'Email',
            'Phone_no',
            'Password']
       
# class StudentRegistrationForm(forms.Form):
#     Student_name= forms.CharField(max_length=50,label="Name",widget=forms.TextInput(attrs={'size':'40','title':'Your Name'}))
#     College_name=forms.CharField(max_length=55,label="College Name",widget=forms.TextInput(attrs={'size':'40','title':'Your Name'}))
#     c=[("B.Sc.Cs.It","B.Sc.Cs.It"),("B.IM","B.IM"),("B.CA","B.CA")]
#     Faculty=forms.ChoiceField(choices=c,label="Faculty")
#     d=[("First","First"),("Second","Second"),("Third","Third"),("Fourth","Fourth"),("Fifth","Fifth"),("Sixth","Sixth"),("Seventh","Seventh"),("Eighth","Eighth")]
#     Semester=forms.ChoiceField(choices=d,label="Semester")
#     Email=forms.EmailField(max_length=50,required=True)
#     Phone_no=forms.IntegerField()
#     Password=forms.CharField(widget=forms.PasswordInput) 



# class LoginForm(forms.ModelForm):
#     class Meta:
#         model=studentlogin 
#         fields=[
#             'email',
#             'password'
#         ]

# class LoginForm(forms.Form):
#     email=forms.CharField(max_length=50,required=True,widget=forms.TextInput)
#     password=forms.CharField(widget=forms.PasswordInput,max_length=50)

#     def clean(self,*args,**kwargs):
#         email=self.cleaned_data.get('email')
#         password=self.cleaned_data.get('password')
#         if email and password:
#             user=authenticate(email=email,password=password)
#             if not user:
#                 raise forms.ValidationError("This user doesnot exist")
#             if not user.check_password(password):
#                 raise forms.ValidationError("Incorrect Password")
#             if not user.is_active:
#                 raise forms.ValidationError("User is not active")
#         return LoginForm()
        
           
class AddeventForm(forms.ModelForm):
    # Eventdate=forms.DateField(widget=forms.SelectDateWidget,label="Date Of Event")
    Eventstarttime=forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    Eventfinishtime=forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    

    class Meta:
        model= Addnewevent
        fields=[
            'Eventname',
            'Eventtheme',
            'Eventvenue',
            'Eventorganizer',
            'Eventmanager',
            'Eventcapacity',
            'Eventperiod',
            'Eventdate',
            'Eventstarttime',
            'Eventfinishtime',
            'Eventlogo'
        ]
