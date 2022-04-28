from django.db import models

# Create your models here.
class UserMaster(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=15)
    otp=models.IntegerField()
    role=models.CharField(max_length=30)
    isActive=models.BooleanField(default=True)
    isVerified=models.BooleanField(default=False)
    isCreated=models.DateTimeField(auto_now_add=True)
    isUpdated=models.DateTimeField(auto_now_add=True)

class Candidate(models.Model):
    userid=models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    contact=models.CharField(max_length=15)
    state=models.CharField(max_length=30)
    city=models.CharField(max_length=20)
    address=models.TextField()
    dob=models.CharField(max_length=15)
    gender=models.CharField(max_length=15)

class Company(models.Model):
    userid=models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    companyname=models.CharField(max_length=100)
    state=models.CharField(max_length=30)
    city=models.CharField(max_length=20)
    address=models.TextField()
    contact=models.CharField(max_length=15)
    
class JobDetails(models.Model):
    userid=models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    companylogo=models.ImageField(upload_to="jobapp/img/company")
    jobname=models.CharField(max_length=200)
    jobtype=models.CharField(max_length=30)
    companyname=models.CharField(max_length=100)
    jobdesc=models.TextField()
    qualification=models.CharField(max_length=50)
    responsibilities=models.TextField()
    location=models.CharField(max_length=50)
    website=models.CharField(max_length=50)
    companyemail=models.EmailField()
    salary=models.CharField(max_length=20)
    experience=models.CharField(max_length=20)
    requirments=models.TextField()
    lastdate=models.CharField(max_length=15)

class Candidate_resume(models.Model):
    resumeid=models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    linkdin=models.CharField(max_length=150)
    github=models.CharField(max_length=150)
    fullname=models.CharField(max_length=40)
    email=models.EmailField()
    contact=models.CharField(max_length=12)
    collegename=models.CharField(max_length=60)
    course=models.CharField(max_length=50)
    passingyear=models.CharField(max_length=6)
    skills=models.CharField(max_length=1000)
    experience=models.CharField(max_length=10)

class Jobapplications(models.Model):
    jobid=models.ForeignKey(Candidate,on_delete=models.CASCADE)
    fullname=models.CharField(max_length=40)
    email=models.EmailField()
    contact=models.CharField(max_length=12)
    experience=models.CharField(max_length=10)
    resume=models.ForeignKey(Candidate_resume,on_delete=models.CASCADE)


