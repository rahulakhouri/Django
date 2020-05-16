from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate,login,logout

from .forms import StudentForm  
from .models import AppUser, CollegeAdmin



# Create your views here.
#@login_required
def hello(request):
   loggedin = request.user.is_authenticated
   if not loggedin:
      return HttpResponseRedirect('/index/')
   if request.user.user_type == AppUser.COLLEGEADMIN:
      ca= CollegeAdmin.objects.get(user = request.user)
      cn = ca.college.college_name
      #template = loader.get_template('colleghome.html') # getting our template  
      return render(request,"college/collegehome.html",{'college_name':cn})  
   template = loader.get_template('index.html') # getting our template  
   return HttpResponse(template.render())       # rendering the template in HttpResponse 

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect('/index/')

def abc(request):
   return HttpResponse("Welcome")

def index(request): 
   if request.method == 'POST': # If the form has been submitted...
        form = StudentForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
               login(request, user)
               return HttpResponseRedirect('/hello/')
            # A backend authenticated the credentials
            else:
               #return HttpResponseRedirect('/index/')
               
               student = StudentForm() 
               html = student.as_p() 
               return render(request,"college/index.html",{'form':html,'message' : "Wrong password"})  
            # No backend authenticated the credentials

            print (form.cleaned_data['firstname'])
   elif request.user.is_authenticated:
         return HttpResponseRedirect('/hello/')
 

   student = StudentForm() 
   html = student.as_p() 
   return render(request,"college/index.html",{'form':html,'age' : 30})  