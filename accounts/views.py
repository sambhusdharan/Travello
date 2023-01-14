from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth,User
# Create your views here.
def register(request):
     if request.method=="POST":
          firstname = request.POST['firstname']
          lastname = request.POST['lastname']
          email = request.POST['email']
          username = request.POST['username']
          password1 = request.POST['password1']
          password2 = request.POST['password2']
          if password1 == password2:
              if User.objects.filter(username=username).exists():
                  messages.info(request,"username already exist")
                  return redirect("register")
              elif User.objects.filter(email=email).exists():
                  messages.info(request," email already exist ")
                  return redirect("register")
              else:
                  user=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password1)
                  user.save()
                  print("user created")
                  return redirect('fun')
          else:
             messages.info(request,"password not matched")
             return redirect('register')

     else:
      # messages.info(request,"password error")
      return render(request, 'registration.html')

def login(request):
    if request.method=='POST':
        username= request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid user")
            return redirect("Login")
    else:
      return render(request,"Login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


def News(request):
    return render(request,'News.html')



def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contacts.html')

# def search(request):
#     if request.method == "POST":
#         city = request.POST['city']
#         departure = request.POST['departure']
#         arrival = request.POST['arrival']
#         budget = request.POST['budget']
#         use = User.objects.create_user(city_search=city,departure_search=departure,arrival_search=arrival,budget_search=budget)
#         use.save()
#         return redirect('/')
#     else:
#         return render(request, '/')