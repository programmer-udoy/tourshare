from django.shortcuts import render



from .models import create_user
from .models import create_team
from .models import join_user
from .models import Room, Message

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import  messages


from django.shortcuts import render ,HttpResponse,redirect








# Create your views here.
def index(request):
    return render(request,'tourshare/home.html')

def about(request):
    return render(request,'tourshare/home.html')


def createteam(request):



    
    if request.method=="POST":

       destination=request.POST.get('destination','')
       email=request.POST.get('email','')
       phone_number=request.POST.get('phone_number','')
       team_member=request.POST.get('team_member')
       needed_member=request.POST.get('needed_member')
       start_date=request.POST.get('start_date','')
       end_date=request.POST.get('end_date','')
       address=request.POST.get('address','')
       fblink=request.POST.get('fblink','')
       twitterlink=request.POST.get('twitterlink','')
       national_id_image=request.FILES['national_id_image']
       create_user_image=request.FILES['create_user_image']

      
       mydata= create_user(destination=destination,email=email,phone_number=phone_number,team_member=team_member,needed_member=needed_member,start_date=start_date,end_date=end_date,address=address,fblink=fblink,twitterlink=twitterlink,national_id_image=national_id_image,create_user_image=create_user_image)
       mydata.save()
    
      
    
    return render(request,'tourshare/create.html')
    
  
      


def jointeam(request):

    showdata=create_team.objects.all()
    
    return render(request,'tourshare/join.html',{'data':showdata})

def checkout(request):
    if request.method=="POST":

         group_name=request.POST.get('group_name','')
         team_member=request.POST.get('team_member')
         email=request.POST.get('email','')
         phone_number=request.POST.get('phone_number','')
         address=request.POST.get('address','')
         fblink=request.POST.get('fblink','')
         twitterlink=request.POST.get('twitterlink','')
         national_id_image=request.FILES['national_id_image']
         join_user_image=request.FILES['join_user_image']
         

      
         mydata= join_user(group_name=group_name,team_member=team_member,email=email,phone_number=phone_number,address=address,fblink=fblink,twitterlink=twitterlink,national_id_image=national_id_image,join_user_image=join_user_image)
         mydata.save()
    return render(request,'tourshare/checkout.html')
    

def signin(request):
    if request.method=="POST":
        uname=request.POST['uname']
        psw=request.POST['psw']
        user=authenticate(username=uname,password=psw)
        if user is not None:
            login(request,user)
            messages.success(request,"succesfully logged in")
            return render(request,'tourshare/signin.html')
        else:
             messages.error(request,"invalid,please try again!")
             return render(request,'tourshare/signin.html')

        
   

    return render(request,'tourshare/signin.html')

def signout(request):
    logout(request)
    messages.success(request,"succesfully signout ")
    return render(request,'tourshare/signout.html')

    
        
       

    

def signup(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        user_name=request.POST['user_name']
        email=request.POST['email']
        password=request.POST['password']
        retype_password=request.POST['retype_password']

        #check the errorneus input
        if len(user_name)<10:
            messages.error(request, " Your user name must be above 10 characters")
            return render(request,'tourshare/signup.html')

        if not user_name.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return render(request,'tourshare/signup.html')
        if (password!= retype_password):
             messages.error(request, " Passwords do not match")
             return render(request,'tourshare/signup.html')
        if User.objects.filter(username = user_name).first():
            messages.error(request, "This username is already taken")
            return render(request,'tourshare/signup.html')

   

        #create the user
        myuser=User.objects.create_user(user_name,email,password)
        myuser.first_name=firstname
        myuser.last_name=lastname
        myuser.save()
       
        messages.success(request,'account created succesfully')
        return render(request,'tourshare/signup.html')
    
     

    return render(request,'tourshare/signup.html')
   
   
    

    

    

def contactus(request):
    return render(request,'tourshare/home.html')


def connect(request):
        return render(request,'tourshare/connect.html')

def room(request, room):
   
    return render(request, 'tourshare/room.html', )
def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return render(request,'tourshare/checkview/' +room+ '/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return render(request,'tourshare/checkview/'+room+'/?username='+username)