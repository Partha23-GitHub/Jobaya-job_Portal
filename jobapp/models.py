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
    profilePic=models.ImageField(upload_to="jobapp/img/candidate")

class Company(models.Model):
    userid=models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    companyname=models.CharField(max_length=100)
    state=models.CharField(max_length=30)
    city=models.CharField(max_length=20)
    address=models.TextField()
    contact=models.CharField(max_length=15)
    logo=models.ImageField(upload_to="jobapp/img/company")
    
class JobDetails(models.Model):
    userid=models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    jobname=models.CharField(max_length=200)
    jobtype=models.CharField(max_length=30)
    companyname=models.CharField(max_length=100)
    jobdesc=models.TextField()
    qualification=models.CharField(max_length=50)
    responsibilities=models.TextField()
    location=models.CharField(max_length=50)
    website=models.CharField(max_length=50)
    companyemail=models.CharField(max_length=50)
    salary=models.CharField(max_length=20)
    experience=models.CharField(max_length=20)
    requirments=models.TextField()
