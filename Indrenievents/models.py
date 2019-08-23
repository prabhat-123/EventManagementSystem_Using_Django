from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date


# Eventtime=models.DateField(verbose_name="Event Date")
# Picture=models.ImageField(upload_to='images/',verbose_name="Event Cover Picture")
# Create your models here.

class Student(models.Model):
    Student_name= models.CharField(max_length=50)
    College_name=models.CharField(max_length=55)
    faculty_choices=(
            ('B.Sc.Cs.It', 'B.Sc.Cs.It') ,
            ('B.CA', 'B.CA'), 
            ('B.IM', 'B.IM')
            )
    sem_choices=(
        ('First', 'First'),
        ('Second','Second'),
        ('Third','Third'),
        ('Fourth','Fourth'),
        ('Fifth','Fifth'),
        ('Sixth','Sixth'),
        ('Seventh','Seventh'),
        ('Eighth','Eighth')
    ) 
    Faculty=models.CharField(max_length=20,choices=faculty_choices)
    Semester=models.CharField(max_length=50,choices=sem_choices)
    Email=models.EmailField(max_length=50)
    Phone_no=models.IntegerField(default=0)
    Password= models.CharField(max_length=50)

    def __str__(self):
        return self.Student_name





class Addnewevent(models.Model):
    Eventname=models.CharField(verbose_name="Event Name",max_length=70)
    Eventtheme=models.TextField(verbose_name="Event Theme",max_length=1500)
    Eventvenue=models.CharField(max_length=50,verbose_name="Event Venue")
    Eventorganizer=models.CharField(max_length=80,verbose_name="Event Organizer")
    Eventmanager=models.CharField(max_length=50,verbose_name="Event Manager")
    Eventcapacity=models.IntegerField(verbose_name="Number Of Guests allowed")
    Eventperiod=models.IntegerField(verbose_name="Event Duration In Days",default="1")
    Eventdate=models.DateField(verbose_name="Date of event",auto_now_add=False,auto_now=False,blank=True,null=True)
    Eventstarttime=models.TimeField(verbose_name="Starting Time of Event",blank=True,null=True)
    Eventfinishtime=models.TimeField(verbose_name="Finishing Time of Event",blank=True,null=True)
    Eventposted=models.TimeField(verbose_name="Time of Post",auto_now_add=True,auto_now=False)
    Eventlogo=models.ImageField(verbose_name="Logo Of Event" ,upload_to='event_logos/',null=True,blank=True)

    def __str__(self):
        return self.Eventname

