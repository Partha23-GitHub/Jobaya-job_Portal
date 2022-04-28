from django.shortcuts import redirect, render
from .models import *
from random import randint

#for index page
def index(request):
     return render(request,'jobapp/index.html')
def candidateIndex(request):
    return render(request,'jobapp/candidateindex.html')

def companyIndex(request):
    id=request.session.get('id')
    postedjobs=JobDetails.objects.filter(userid=id).order_by('lastdate')[:5]
    return render(request,'jobapp/company/index.html',{'jobs':postedjobs})

#for sign Up
def signUp(request):
    return render(request,'jobapp/signup.html')

#for User registration
def registerUser(request):
    if request.POST['role']=='Candidate':
        role=request.POST['role']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if UserMaster.objects.filter(email=email):
            return render(request,'jobapp/login.html',{'message':'user already exist,Please Login'})
        else:
            if password==cpassword:
                otp=randint(10000,99999)
                newUser=UserMaster.objects.create(role=role,email=email,otp=otp,password=password)
                newcandidate=Candidate.objects.create(userid=newUser,firstname=firstname,lastname=lastname)
                return render(request,'jobapp/otpverify.html',{'email':email})

    elif request.POST['role']=='Company':
            role=request.POST['role']
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            email=request.POST['email']
            password=request.POST['password']
            cpassword=request.POST['cpassword']
            if UserMaster.objects.filter(email=email):
                return render(request,'jobapp/login.html',{'message':'user already exist,Please Login'})
            else:
                if password==cpassword:
                    otp=randint(10000,99999)
                    newUser=UserMaster.objects.create(role=role,email=email,otp=otp,password=password)
                    newcompany=Company.objects.create(userid=newUser,firstname=firstname,lastname=lastname)
                    return render(request,'jobapp/otpverify.html',{'email':email})
    else:
        return redirect('signup')

#for rensering OTPpage
def otpPage(request):
    return render(request,'jobapp/otpverify.html')

#for OTP verifyPage and then rendering Login page
def otpVerify(request):
    email=request.POST['registeremail']
    inputotp=int(request.POST['inputotp'])
    user=UserMaster.objects.get(email=email)
    if user:
        if user.otp==inputotp:
            return render(request,'jobapp/login.html',{'message':'Registration successfull, Please login'})
        else:
            return render(request,'jobapp/otpverify.html',{'message':'Otp does not matched','email':user.email})
    else:
        return render(request,'jobapp/signup.html')

def loginPage(request):
    return render(request,'jobapp/login.html')

#User Login view
def loginUser(request):
    #login as a candidate
    if request.POST['role']=='Candidate':
        email=request.POST['email']
        password=request.POST['password']
        try:
            user=UserMaster.objects.get(email=email)
            if user:
                if user.password==password and user.role=='Candidate':
                    candidate=Candidate.objects.get(userid=user)
                    request.session['id']=user.id
                    request.session['role']=user.role
                    request.session['firstname']=candidate.firstname
                    request.session['lastname']=candidate.lastname
                    request.session['email']=user.email
                    request.session['password']=user.password
                    return redirect('candidateindex')
                else:
                    return render(request,'jobapp/login.html',{'message':'Password or Role does not matched'})
        except:
            return render(request,'jobapp/login.html',{'message':'User doesnot exist,Please SignUp '})
    #login as a company
    elif request.POST['role']=='Company':
        email=request.POST['email']
        password=request.POST['password']
        try:
            user=UserMaster.objects.get(email=email)
            if user:
                if user.password==password and user.role=='Company':
                    company=Company.objects.get(userid=user)
                    request.session['id']=user.id
                    request.session['role']=user.role
                    request.session['firstname']=company.firstname
                    request.session['lastname']=company.lastname
                    request.session['email']=user.email
                    request.session['companyname']=company.companyname
                    request.session['password']=user.password
                    return redirect('companyindex')
                else:
                    return render(request,'jobapp/login.html',{'message':'Password or Role does not matched'})
        except:
            return render(request,'jobapp/login.html',{'message':'User doesnot exist,Please SignUp'})
    #if user nothing choose
    else:
        return render(request,'jobapp/login.html',{'message':'Please choose a Role'})


#candidateprofile view
def CandidateProfileView(request,pk):
    user=UserMaster.objects.get(pk=pk)
    candidate=Candidate.objects.get(userid=user)
    return render(request,'jobapp/candidateprofile.html',{'user':user,'candidate':candidate})

#companyprofile view
def CompanyProfileView(request,pk):
    user=UserMaster.objects.get(pk=pk)
    company=Company.objects.get(userid=user)
    return render(request,'jobapp/company/companyprofile.html',{'user':user,'company':company})

#update candidateProfile
def updateProfile(request,pk):
    user=UserMaster.objects.get(pk=pk)
    if user.role=='Candidate':
        candidate=Candidate.objects.get(userid=user)
        candidate.contact=request.POST['contact']
        candidate.city=request.POST['city']
        candidate.state=request.POST['state']
        candidate.dob=request.POST['dob']
        candidate.address=request.POST['address']
        candidate.gender=request.POST['gender']
        candidate.save()
        #formating URL
        url= f'/candidateprofile/{pk}'
        return redirect(url)

    if user.role=='Company':
        company=Company.objects.get(userid=user)
        company.contact=request.POST['contact']
        company.companyname=request.POST['companyname']
        company.city=request.POST['city']
        company.state=request.POST['state']
        company.address=request.POST['address']
        company.save()
        #formating URL
        url= f'/companyprofile/{pk}'
        return redirect(url)

def jobPostPage(request):
    return render(request,'jobapp/company/post-a-job.html')

def JobdetailsSubmit(request):
    jobposteremail=request.session.get('email')
    id=UserMaster.objects.get(email=jobposteremail)
    if id.role=='Company':
        jobname=request.POST['jobtitle']
        jobtype=request.POST['jobtype']
        companyname=request.POST['companyname']
        companyemail=request.POST['email']
        location=request.POST['location']
        qualification=request.POST['qualification']
        jobdesc=request.POST['jobdesc']
        website=request.POST['website']
        salary=request.POST['salary']
        experience=request.POST['experience']
        responsibilities=request.POST['responsibility']
        requirments=request.POST['requirments']
        lastdate=request.POST['lastdate']

        newjob=JobDetails.objects.create(userid=id,jobname=jobname,jobtype=jobtype,companyname=companyname,companyemail=companyemail,
        location=location,qualification=qualification,jobdesc=jobdesc,website=website,salary=salary,
        experience=experience,responsibilities=responsibilities,requirments=requirments,lastdate=lastdate)
        return render(request,'jobapp/company/post-a-job.html',{'message':'You have successfully posted this job'})

# display joblist posted by perticular HR
def companyjoblist(request):
    id=request.session.get('id')
    postedjobs=JobDetails.objects.filter(userid=id).order_by('lastdate')
    return render(request,'jobapp/company/companyjoblist.html',{'jobs':postedjobs})

#display all jobs to candidate
def candidateJobList(request):
    alljobs=JobDetails.objects.all().order_by('lastdate')
    return render(request,'jobapp/job-list.html',{'alljobs':alljobs})

#view job details
def viewjobDetails(request,pk):
    job=JobDetails.objects.get(userid=pk)
    return render(request,'jobapp/job-details.html',{'job':job})

# Logout System
def companyLogout(request):
    del request.session['email']
    del request.session['password']
    return redirect('indexpage')

def candidateLogout(request):
    del request.session['email']
    del request.session['password']
    return redirect('indexpage')