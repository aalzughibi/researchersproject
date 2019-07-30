from django.shortcuts import render,reverse,redirect, get_object_or_404
from django.http import Http404,HttpResponseRedirect
from .models import profileModel,aboutResearch
from .form import UserForm,ProfileForm,LoginForm,aboutResearchForm,rateingForm,contactForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import ProfileSerializer,UserSerializer,aboutResearchSerializer
from django.core.mail import send_mail
from django.conf import settings

def home(req):
    data = profileModel.objects.all().filter(select='R')
    #testing
    userinfo = User.objects.all()
    return render(req,'home.html',context={'data':data,'userinfo':userinfo})

@login_required
def Logout(req):
    logout(req)
    return HttpResponseRedirect(reverse('home'))

def Login(req):
    form = LoginForm()
    if req.method =='POST':
        form = LoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(req,user)
                    return HttpResponseRedirect(reverse('home'))
                else:
                    messages.error(req,'user is not active')
            else:
                messages.error(req,'invalid username or password,Try Again')
    return render(req,'login.html',context={'loginform':form})

def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['mrabdullah0102@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('home')

def Registertion(req):
    UserFo = UserForm()
    ProfileFo = ProfileForm()
    if req.method =='POST':
        UserFo = UserForm(req.POST)
        ProfileFo = ProfileForm(req.POST)
        if UserFo.is_valid and ProfileFo.is_valid:
            user = UserFo.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = ProfileFo.save(commit=False)
            profile.user = user
            profile.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return Http404()
    return render(req,'reg.html',context={'userForm':UserFo,'ProfileForm':ProfileFo})
@login_required
def addResearch(req):
    ResForm = aboutResearchForm()
    if req.method=='POST':
        ResForm = aboutResearchForm(req.POST)
        if ResForm.is_valid():
            Resr=ResForm.save(commit=False)
            Resr.user = req.user
            Resr.save()
            return HttpResponseRedirect(reverse('home'))
    return render(req,'addresearch.html',context={'data':ResForm})

def getReasearch(req):
    aa = aboutResearch.objects.all()
    return render(req,'home.html',context={"aa":aa})

@login_required
def GetResearchers(req):
    data = profileModel.objects.all().filter(select='R')
    return render(req,'researchers.html',context={'data':data,})

@login_required
def rate(req, pk):
    data = rateingForm()
    if req.method=='POST':
        data = rateingForm(req.POST)
        if data.is_valid():
            user = profileModel.objects.get(id=pk)
            user.rating =user.rating+ data.cleaned_data['rate']
            x = user.rating
            user.count +=1
            y=user.count
            z=float(x/y)
            user.aver = z
            user.save()
            return HttpResponseRedirect(reverse('home'))
    return render(req,'rate.html',context={'data':data})

@login_required
def details(req,pk):
    try:
        researcher = profileModel.objects.get(id=pk)
        if req.method=='POST':
            body = 'name:'+req.user.first_name + req.user.last_name + '\n'+'email:'+req.user.email+'\n Phone:'
            send_mail('Request Assistant Researcher',body,settings.EMAIL_HOST_USER,[researcher.user.email])
            return redirect('home')
    except:
        raise Http404()
    return render(req,'details.html',context={'data':researcher})

class aboutResearchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=aboutResearch.objects.all()
    serializer_class = aboutResearchSerializer
    
class profileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=profileModel.objects.all()
    serializer_class = ProfileSerializer

    
class userViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def detailsResearch(req,pk):
    data = aboutResearch.objects.get(id=pk)
    if req.method =='POST':
        body = 'name:'+req.user.first_name + req.user.last_name + '\n'+'email:'+req.user.email
        send_mail('request sharing in research',body,settings.EMAIL_HOST_USER,[data.user.email])
    return render(req,'detailsResearch.html',context={'data':data})

@login_required
def sendContact(req):
    form = contactForm()
    if req.method == 'POST':
        form = contactForm(req.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.user = req.user
            send_mail( 'contact', '(email:'+info.user.email+')\n Body:'+info.body , settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER] )
            info.save()
            return HttpResponseRedirect(reverse('home'))
    return render(req,'contact.html',context={'form':form})
@login_required
def profile_details(req,str):
    info =profileModel.objects.get(user=str)
    return render(req,'profiledetails.html',context={'info':info})