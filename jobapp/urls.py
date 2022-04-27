from django.urls import path
from .import views

urlpatterns = [
   path('',views.index,name='indexpage'),
   path('register/',views.registerUser,name='register'),
   path('signup/',views.signUp,name='signup'),
   path('otppage/',views.otpPage,name='otppage'),
   path('otpverify/',views.otpVerify,name='otpverify'),
   path('loginpage/',views.loginPage,name='loginpage'),
   path('login/',views.loginUser,name='loginview'),
   path('updateprofile/<int:pk>',views.updateProfile,name='updateprofile'),
 
   ############### Candidate #################
   path('home/',views.candidateIndex,name='candidateindex'), 
   path('candidateprofile/<int:pk>',views.CandidateProfileView,name='candidateprofile'),
   path('companylogout/',views.candidateLogout,name='candidatelogout'),
   path('alljobs/',views.candidateJobList,name='candidatejobs'),

   ################# Company ##################
   path('company/',views.companyIndex,name='companyindex'),
   path('companyprofile/<int:pk>',views.CompanyProfileView,name='companyprofile'),
   path('postjobpage/',views.jobPostPage,name='postjobpage'),
   path('postjob/',views.JobdetailsSubmit,name='postajob'),
   path('companylogout/',views.companyLogout,name='companylogout'),
   path('companyjoblist/',views.companyjoblist,name='companyjoblist'),
]